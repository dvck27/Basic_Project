from __future__ import annotations

import os
from pathlib import Path
import shutil
from typing import Annotated

from fastapi import FastAPI, File, Form, Request, UploadFile
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from .db import Database
from .gateways import (
    GmailOtpProvider,
    PaiwebBrowserGateway,
    PaiwebSessionConfig,
    SimulatorGateway,
)
from .importer import import_workbook, select_batch
from .models import RuntimeDefaults
from .workflow import WorkflowEngine


PACKAGE_DIR = Path(__file__).resolve().parent
RUNTIME_DIR = Path(os.getenv("PAI_AUTO_HOME", Path.cwd() / "runtime")).resolve()
UPLOAD_DIR = RUNTIME_DIR / "uploads"
DB_PATH = RUNTIME_DIR / "pai_auto.db"
REAL_MAX_ROWS = int(os.getenv("PAI_AUTO_REAL_MAX_ROWS", "1"))
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

templates = Jinja2Templates(directory=str(PACKAGE_DIR / "templates"))
db = Database(DB_PATH)
engine = WorkflowEngine(db)

app = FastAPI(title="PAI Auto", docs_url=None, redoc_url=None)


def _context(request: Request, **extra):
    return {
        "request": request,
        "runs": db.recent_runs(),
        "runtime_dir": str(RUNTIME_DIR),
        "real_max_rows": REAL_MAX_ROWS,
        **extra,
    }


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", _context(request))


@app.post("/import", response_class=HTMLResponse)
def upload_source(request: Request, file: UploadFile = File(...)):
    if not file.filename or not file.filename.lower().endswith(".xlsx"):
        return templates.TemplateResponse(
            "index.html",
            _context(request, error="Selecciona un archivo .xlsx."),
            status_code=400,
        )
    target = UPLOAD_DIR / Path(file.filename).name
    with target.open("wb") as stream:
        shutil.copyfileobj(file.file, stream)
    try:
        result = import_workbook(target)
    except Exception as exc:
        return templates.TemplateResponse(
            "index.html", _context(request, error=str(exc)), status_code=400
        )
    return templates.TemplateResponse(
        "index.html", _context(request, source=target.name, preview=result)
    )


@app.post("/run", response_class=HTMLResponse)
def run_workflow(
    request: Request,
    source: Annotated[str, Form()],
    start_row: Annotated[int, Form()] = 16,
    batch_size: Annotated[int, Form()] = 20,
    mode: Annotated[str, Form()] = "simulator",
    units: Annotated[str, Form()] = "",
    anatomical_site: Annotated[str, Form()] = "",
    application_type: Annotated[str, Form()] = "",
    economic_sector: Annotated[str, Form()] = "",
    base_url: Annotated[str, Form()] = "https://paiweb2.paiweb.gov.co",
    id_type: Annotated[str, Form()] = "Cédula de ciudadanía",
    username: Annotated[str, Form()] = "",
    password: Annotated[str, Form()] = "",
    site: Annotated[str, Form()] = "",
    gmail_token_file: Annotated[str, Form()] = "",
    gmail_query: Annotated[str, Form()] = "newer_than:10m",
    confirm_real: Annotated[bool, Form()] = False,
):
    source_path = UPLOAD_DIR / Path(source).name
    if not source_path.exists():
        return templates.TemplateResponse(
            "index.html",
            _context(request, error="La fuente ya no existe en runtime/uploads."),
            status_code=404,
        )
    imported = import_workbook(source_path)
    records = select_batch(imported.records, start_source_row=start_row, batch_size=batch_size)
    if not records:
        return templates.TemplateResponse(
            "index.html",
            _context(
                request,
                source=source,
                preview=imported,
                error="No hay aplicaciones válidas en ese rango.",
            ),
            status_code=400,
        )
    defaults = RuntimeDefaults(units, anatomical_site, application_type, economic_sector)
    if mode == "simulator":
        gateway = SimulatorGateway()
    elif mode == "real":
        selected_rows = len({record.source_row for record in records})
        if selected_rows > REAL_MAX_ROWS:
            return templates.TemplateResponse(
                "index.html",
                _context(
                    request,
                    source=source,
                    preview=imported,
                    error=(
                        f"Modo real limitado a {REAL_MAX_ROWS} fila(s) en este equipo. "
                        "Ajusta PAI_AUTO_REAL_MAX_ROWS después de validar la corrida de una fila."
                    ),
                ),
                status_code=400,
            )
        if not confirm_real:
            return templates.TemplateResponse(
                "index.html",
                _context(
                    request,
                    source=source,
                    preview=imported,
                    error=(
                        "Modo real: debes confirmar explícitamente que esta corrida escribirá en PAIWEB."
                    ),
                ),
                status_code=400,
            )
        if not all([units, anatomical_site, application_type, economic_sector]):
            return templates.TemplateResponse(
                "index.html",
                _context(
                    request,
                    source=source,
                    preview=imported,
                    error=(
                        "Modo real: define unidades, sitio anatómico, tipo de aplicación y "
                        "sector económico. No se usan valores implícitos."
                    ),
                ),
                status_code=400,
            )
        if not all([username, password, site, gmail_token_file]):
            return templates.TemplateResponse(
                "index.html",
                _context(
                    request,
                    source=source,
                    preview=imported,
                    error=(
                        "Modo real: faltan usuario, contraseña, sede o token OAuth de Gmail."
                    ),
                ),
                status_code=400,
            )
        gateway = PaiwebBrowserGateway(
            PaiwebSessionConfig(base_url, id_type, username, password, site, headless=False),
            GmailOtpProvider(gmail_token_file, gmail_query),
        )
    else:
        return templates.TemplateResponse(
            "index.html", _context(request, error="Modo inválido."), status_code=400
        )

    try:
        outcome = engine.run(
            source_name=source,
            records=records,
            batch_size=batch_size,
            mode=mode,
            gateway=gateway,
            defaults=defaults,
        )
    except Exception as exc:
        return templates.TemplateResponse(
            "index.html",
            _context(
                request,
                source=source,
                preview=imported,
                error=f"La ejecución se abortó: {exc}",
            ),
            status_code=500,
        )
    return RedirectResponse(url=f"/runs/{outcome.run_id}", status_code=303)


@app.get("/runs/{run_id}", response_class=HTMLResponse)
def run_detail(request: Request, run_id: str):
    items = db.run_items(run_id)
    return templates.TemplateResponse(
        "index.html", _context(request, selected_run=run_id, items=items)
    )
