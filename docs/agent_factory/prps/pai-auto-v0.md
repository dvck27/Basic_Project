# PRP: PAI Auto v0 — flujo compacto local

## Problem
El repositorio original demostró gran parte de la lectura y del comportamiento de PAIWEB, pero acumuló una arquitectura institucional extensa. Se necesita una implementación paralela, compacta, operable por una sola persona y útil para pruebas inmediatas.

## Objective
Tener un flujo local end-to-end desde XLSX hasta escritura/verificación mediante gateway, con simulador plenamente ejecutable y adaptador real listo para validar una fila.

## Current Context
`Basic_Project` era un bootstrap agent-ready sin stack. `vacunacion-paiweb` aporta contrato de 222 columnas, descomposición, selectores 2026, login/OTP/sede y contrato del formulario.

## Scope
- Python/FastAPI UI local.
- SQLite.
- Importación `Vacunación SIS` 222 columnas, PAI BN:FF.
- 1/20/50/100 filas.
- Idempotencia y ejecución que continúa tras fallos individuales.
- Simulador.
- Playwright real + Gmail OTP readonly.
- Administrador único y confirmación por corrida.

## Out of Scope
- Biológicos particulares FG:HJ.
- Alta/modificación de pacientes.
- Autorizaciones clínicas y solicitudes de cambio.
- LLM en camino crítico.
- Servidor corporativo, SQL Server, Docker, Redis.
- EXE empaquetado en esta iteración.

## Proposed Design
`app.py → importer.py → workflow.py → Gateway → verify → db.py`.

El Gateway es intercambiable; simulator y PAIWEB usan el mismo contrato. `select_batch` elige filas fuente distintas y conserva todas sus aplicaciones.

## Risks
- Los literales/selectores reales pueden cambiar.
- El proyecto original nunca había ejecutado una escritura real.
- Un valor operativo incorrecto repetido a todo un lote sería consistente pero incorrecto; por eso en real los cuatro defaults son obligatorios y no se precargan.
- PII permanece en runtime local; nunca en Git.

## Validation
- pytest: libro sintético 222 columnas.
- pytest: una fila con múltiples aplicaciones sigue siendo lote de una fila.
- pytest: simulator write + verify.
- pytest: repetición omite por idempotencia.
- smoke: GET `/` 200.
- pendiente: corrida real de 1 fila autorizada.

## Rollback Plan
La implementación vive en `feature/pai-auto-v0`; `main` no se modifica hasta merge. El runtime local puede eliminarse sin afectar el repositorio.

## Acceptance Criteria
- [x] Motor e interfaz implementados.
- [x] Lotes por fila 1/20/50/100.
- [x] Simulador end-to-end.
- [x] Idempotencia local.
- [x] Adaptador real implementado.
- [x] Docs y contrato sincronizados.
- [x] Tests locales en verde.
- [ ] Primera escritura real validada contra PAIWEB.
- [ ] Tras esa validación, confirmar/calibrar selectores y habilitar lote real >1.
