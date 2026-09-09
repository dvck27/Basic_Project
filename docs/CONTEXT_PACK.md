# Context Pack — PAI Auto

## Qué es
`Basic_Project` aloja ahora **PAI Auto**, una implementación compacta local-first para procesar el
Registro Diario SIS hacia PAIWEB. Se construyó usando `dvck27/vacunacion-paiweb` como fuente de
conocimiento, no como base de código a copiar.

## Objetivo operativo
Un único administrador carga un XLSX, revisa el diagnóstico y ejecuta por 1/20/50/100 **filas fuente**.
El motor descompone cada fila en aplicaciones PAI, evita reenvíos por huella local, escribe mediante un
gateway y verifica antes de confirmar.

## Stack
- Python >=3.11
- FastAPI + Jinja2
- SQLite
- openpyxl
- Playwright + Google Gmail API como extras para modo real

## Entry points
- CLI/UI: `pai-auto` → `pai_auto.main:main`
- Web: `src/pai_auto/app.py`
- Importador: `src/pai_auto/importer.py`
- Workflow: `src/pai_auto/workflow.py`
- Gateways: `src/pai_auto/gateways.py`
- Persistencia: `src/pai_auto/db.py`

## Contrato del origen
- Hoja `Vacunación SIS`
- 222 columnas
- datos desde fila 16
- PAI `BN:FF`, 28 grupos
- particulares `FG:HJ` fuera de alcance V0
- control local `HK:HN`; `HK` se usa como vacunador

Una fila puede producir varias aplicaciones. `batch_size` siempre significa **número de filas fuente**,
no número de aplicaciones.

## Modos
### simulator
Completo y local. Es la vía normal para pruebas funcionales.

### real
Playwright navega PAIWEB y Gmail OAuth readonly obtiene el OTP. El administrador debe confirmar la
escritura, introducir valores operativos sin defaults implícitos y respetar `PAI_AUTO_REAL_MAX_ROWS`
(default 1 hasta validar el primer envío real).

## Persistencia
`runtime/pai_auto.db` mantiene ejecuciones, ítems e identificadores procesados. La huella de idempotencia
combina tipo/número de documento, fecha, código/tipo de biológico, dosis y lote. Solo se marca procesado
después de `verify()`.

## Secretos
No versionar credenciales, tokens, cookies, archivos OAuth ni datos reales. La contraseña PAIWEB entra por
formulario y no se persiste. El token Gmail se referencia por ruta local.

## LLM
Fuera del camino crítico V0. Puede agregarse como nodo opcional de asistencia, nunca como autoridad para
identidad, biológico, dosis, lote o decisión clínica.

## Estado verificable
- Tests locales de importación, selección de filas, simulador e idempotencia: implementados.
- UI FastAPI: implementada.
- Real browser adapter: implementado desde el mapeo observado del repo original, pendiente de validar una
  escritura real; el proyecto fuente no había realizado una escritura real.
- Paquetes portables/EXE: pendiente; `INICIAR.bat` deja el entorno autocontenido en `.venv`.

## Cómo retomar
1. `AGENTS.md`
2. este archivo
3. `specs/WORKFLOW.md`
4. `docs/agent_factory/prps/pai-auto-v0.md`
5. `docs/DECISION_LOG.md`
6. código + tests
