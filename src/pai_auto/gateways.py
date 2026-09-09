from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import re
from typing import Protocol

from .models import ApplicationRecord, RuntimeDefaults, WriteResult


class Gateway(Protocol):
    def start(self) -> None: ...
    def write(self, record: ApplicationRecord, defaults: RuntimeDefaults) -> WriteResult: ...
    def verify(self, record: ApplicationRecord, result: WriteResult) -> bool: ...
    def close(self) -> None: ...


class SimulatorGateway:
    def __init__(self):
        self._written: dict[str, str] = {}

    def start(self) -> None:
        return None

    def write(self, record: ApplicationRecord, defaults: RuntimeDefaults) -> WriteResult:
        ref = self._written.setdefault(record.fingerprint, f"SIM-{record.fingerprint[:12]}")
        return WriteResult(ref, f"Simulado {record.biologic_name} / fila {record.source_row}")

    def verify(self, record: ApplicationRecord, result: WriteResult) -> bool:
        return self._written.get(record.fingerprint) == result.remote_ref

    def close(self) -> None:
        return None


class OtpProvider(Protocol):
    def get_code(self) -> str: ...


@dataclass(slots=True)
class GmailOtpProvider:
    token_file: str
    query: str = "newer_than:10m"
    code_pattern: str = r"\b(\d{6})\b"

    def get_code(self) -> str:
        try:
            from google.oauth2.credentials import Credentials
            from googleapiclient.discovery import build
        except ImportError as exc:  # pragma: no cover
            raise RuntimeError("Instala el extra real: pip install -e '.[real]'") from exc
        credentials = Credentials.from_authorized_user_file(
            self.token_file, ["https://www.googleapis.com/auth/gmail.readonly"]
        )
        service = build("gmail", "v1", credentials=credentials, cache_discovery=False)
        result = service.users().messages().list(userId="me", q=self.query, maxResults=10).execute()
        for item in result.get("messages", []):
            msg = service.users().messages().get(userId="me", id=item["id"], format="full").execute()
            match = re.search(self.code_pattern, msg.get("snippet", ""))
            if match:
                return match.group(1)
        raise RuntimeError("No se encontró un OTP reciente que cumpla el patrón configurado.")


@dataclass(slots=True)
class PaiwebSessionConfig:
    base_url: str
    id_type: str
    username: str
    password: str
    site: str
    headless: bool = False


class PaiwebBrowserGateway:
    """Adaptador Playwright compacto basado en el levantamiento PAIWEB 2026."""

    def __init__(self, config: PaiwebSessionConfig, otp: OtpProvider):
        self.config = config
        self.otp = otp
        self._playwright = None
        self._browser = None
        self._page = None

    @property
    def page(self):
        if self._page is None:
            raise RuntimeError("La sesión PAIWEB no está iniciada.")
        return self._page

    def start(self) -> None:
        try:
            from playwright.sync_api import sync_playwright
        except ImportError as exc:  # pragma: no cover
            raise RuntimeError(
                "Instala el extra real: pip install -e '.[real]' y playwright install chromium"
            ) from exc
        self._playwright = sync_playwright().start()
        self._browser = self._playwright.chromium.launch(headless=self.config.headless)
        context = self._browser.new_context()
        self._page = context.new_page()
        self._login()

    def _click_button(self, pattern: str) -> None:
        self.page.get_by_role("button", name=re.compile(pattern, re.I)).first.click()

    def _choose(self, host_selector: str, text: str) -> None:
        host = self.page.locator(host_selector).first
        host.locator(".ng-select-container").click()
        self.page.get_by_role("option", name=text, exact=True).click()

    def _choose_by_control(self, control: str, text: str) -> None:
        host = self.page.locator(f'[formControlName="{control}"]').first
        host.locator(".ng-select-container").click()
        self.page.get_by_role("option", name=text, exact=True).click()

    def _login(self) -> None:
        page = self.page
        page.goto(f"{self.config.base_url.rstrip('/')}/login", wait_until="domcontentloaded")
        page.locator("#contrasena").wait_for(state="visible", timeout=30_000)
        self._choose("#tipoId", self.config.id_type)
        page.locator("#identificacion").fill(self.config.username)
        page.locator("#contrasena").fill(self.config.password)
        self._click_button(r"Ingresar")

        page.wait_for_timeout(700)
        if "doblefactor" in page.url.lower() or page.get_by_text(
            re.compile("Autenticación de usuario", re.I)
        ).count():
            code = self.otp.get_code()
            digit_boxes = page.locator('input[maxlength="1"]')
            if digit_boxes.count() >= len(code):
                for pos, digit in enumerate(code):
                    digit_boxes.nth(pos).fill(digit)
            else:
                page.locator('input[type="text"], input[type="number"], input[type="tel"]').last.fill(code)
            self._click_button(r"Continuar|Validar|Aceptar|Ingresar")

        page.wait_for_timeout(700)
        if "seleccionar" in page.url.lower() or page.get_by_text(
            re.compile("Instituciones", re.I)
        ).count():
            self._choose("ng-select", self.config.site)
            self._click_button(r"Continuar|Ingresar|Aceptar|Seleccionar")
        page.wait_for_load_state("networkidle")

    def _open_patient(self, record: ApplicationRecord) -> None:
        page = self.page
        page.goto(f"{self.config.base_url.rstrip('/')}/biologicos", wait_until="domcontentloaded")
        page.locator("#numeroId").fill(record.document_number)
        self._click_button(r"BUSCAR")
        row = page.locator("datatable-body-row", has_text=record.document_number).first
        if row.count() == 0:
            row = page.locator("tr", has_text=record.document_number).first
        if row.count() == 0:
            raise RuntimeError(f"Paciente {record.document_number}: sin resultado único visible.")
        row.get_by_role("button", name=re.compile(r"DETALLE", re.I)).click()
        page.get_by_text(re.compile("Datos Básicos|Detalle de usuario", re.I)).first.wait_for(
            timeout=20_000
        )
        page.get_by_role(
            "button", name=re.compile(r"APLICACIÓN DE BIOLÓGICOS", re.I)
        ).first.click()
        page.get_by_text(re.compile("Esquema de vacunación|Biológico", re.I)).first.wait_for(
            timeout=20_000
        )

    def _open_application_form(self, record: ApplicationRecord) -> None:
        page = self.page
        if page.locator("#pageSizeId").count():
            try:
                self._choose("#pageSizeId", "60")
            except Exception:
                pass
        row = page.locator("datatable-body-row", has_text=record.biologic_name).filter(
            has_text=record.dose
        ).first
        if row.count() == 0:
            row = page.locator("tr", has_text=record.biologic_name).filter(
                has_text=record.dose
            ).first
        if row.count() == 0:
            raise RuntimeError(
                f"No se encontró línea de esquema para {record.biologic_name} / dosis {record.dose}."
            )
        row.get_by_role("button", name=re.compile(r"REGISTRO", re.I)).click()
        page.locator('[formControlName="fechaAplicacion"]').first.wait_for(timeout=20_000)

    def _fill_form(self, record: ApplicationRecord, defaults: RuntimeDefaults) -> None:
        page = self.page
        page.locator('[formControlName="fechaAplicacion"]').first.fill(
            record.vaccination_date.strftime("%d/%m/%Y")
        )
        page.wait_for_timeout(900)
        self._choose_by_control("numeroUnidades", defaults.units)
        self._choose_by_control("loteBiologico", record.lot)
        if record.diluent_lot and page.locator('[formControlName="loteDiluyente"]').count():
            self._choose_by_control("loteDiluyente", record.diluent_lot)
        if record.syringe_lot and page.locator('[formControlName="loteJeringa"]').count():
            self._choose_by_control("loteJeringa", record.syringe_lot)
        if record.vaccinator and page.locator('[formControlName="nombreVacunador"]').count():
            self._choose_by_control("nombreVacunador", record.vaccinator)
        if defaults.anatomical_site and page.locator(
            '[formControlName="sitioAnatomicoAplicacion"]'
        ).count():
            self._choose_by_control("sitioAnatomicoAplicacion", defaults.anatomical_site)
        if defaults.application_type and page.locator('[formControlName="tipoAplicacion"]').count():
            self._choose_by_control("tipoAplicacion", defaults.application_type)
        if defaults.economic_sector and page.locator('[formControlName="sectorEconomico"]').count():
            self._choose_by_control("sectorEconomico", defaults.economic_sector)

    def write(self, record: ApplicationRecord, defaults: RuntimeDefaults) -> WriteResult:
        self._open_patient(record)
        self._open_application_form(record)
        self._fill_form(record, defaults)
        self._click_button(r"Guardar")
        self.page.get_by_text(re.compile("datos registrados.*correctos", re.I)).wait_for(
            timeout=15_000
        )
        self._click_button(r"Aceptar")
        self.page.get_by_text(re.compile("registrad[ao] exitosamente", re.I)).wait_for(
            timeout=30_000
        )
        self._click_button(r"Aceptar")
        ref = self.page.url.rstrip("/").split("/")[-1]
        return WriteResult(
            ref or f"PAIWEB-{datetime.now(timezone.utc).timestamp():.0f}", self.page.url
        )

    def verify(self, record: ApplicationRecord, result: WriteResult) -> bool:
        self.page.wait_for_load_state("domcontentloaded")
        body = self.page.locator("body").inner_text()
        return record.biologic_name.lower() in body.lower() or result.remote_ref in self.page.url

    def close(self) -> None:
        if self._browser is not None:
            self._browser.close()
        if self._playwright is not None:
            self._playwright.stop()
        self._page = self._browser = self._playwright = None
