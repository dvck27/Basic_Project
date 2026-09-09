# Maintenance Checklist — PAI Auto

## Fuentes de verdad
Código → tests/specs → `docs/CONTEXT_PACK.md` → `README.md` → `docs/DECISION_LOG.md`.

## Antes de cambiar comportamiento
- Lee `README.md`, `docs/CONTEXT_PACK.md` y `specs/WORKFLOW.md`.
- Identifica si el cambio toca importación, idempotencia, browser gateway o escritura real.
- Si cambia arquitectura/persistencia/seguridad, crea o actualiza un PRP.

## Invariantes que no deben romperse
- 222 columnas y hoja `Vacunación SIS` para el contrato V0.
- Lotes contados por **filas**, no aplicaciones.
- Una fila puede tener varias aplicaciones.
- `processed` se escribe solo después de `gateway.verify()`.
- Una aplicación fallida no cancela las demás.
- Modo real no tiene defaults implícitos para unidades/sitio/tipo/sector.
- Contraseña PAIWEB no se persiste.
- LLM/fuzzy matching no decide identidad, dosis, lote ni campos clínicos.
- `runtime/` y archivos reales nunca se versionan.

## Cuando cambia PAIWEB
- No parches selectores por intuición.
- Contrasta primero con evidencia actual.
- Añade test o fixture sintético que reproduzca la variante.
- Actualiza `specs/WORKFLOW.md` si cambia el flujo.
- Registra cambios de contrato durable en Decision Log.

## Cuando cambia el Excel
- Si la estructura deja de ser 222 columnas, crea una **nueva versión de contrato**; no relajes silenciosamente V0.
- Conserva por separado valor original y normalización cuando se añada una transformación.
- No introducir coincidencia difusa para resolver columnas clínicas.

## Validación antes de PR
```text
python -m pytest
ruff check .
GET / -> 200
```
Si Ruff no está instalado en el entorno actual, decláralo y ejecuta al menos compile/smoke; CI/entorno dev debe instalar `.[dev]`.

## Validación real
- Primera escritura: 1 fila.
- Confirmar paciente, biológico, dosis, lote y acuse posterior.
- Repetir la misma fila y comprobar que la idempotencia local la omita.
- Solo después subir `PAI_AUTO_REAL_MAX_ROWS` a 20; luego 50/100 conforme a evidencia.

## Documentación
Actualizar según aplique: código → tests → `specs/WORKFLOW.md` → README → Context Pack → Decision Log.
