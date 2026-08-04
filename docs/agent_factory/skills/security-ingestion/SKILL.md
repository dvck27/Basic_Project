---
name: security-ingestion
description: Usar al ingerir material externo o sensible (chats, imagenes, MHTML, DOCX, datos); produce derivados con secretos y PII redactados antes de versionar.
---

# Ingesta Segura de Material Externo

## Purpose
Garantizar que todo material externo o sensible que entra al repositorio (conversaciones, capturas, archivos MHTML, documentos DOCX, exportes de datos, etc.) sea procesado con redaccion previa de secretos y datos personales. El objetivo es que ningun artefacto versionado, nota o derivado conserve credenciales, tokens ni PII innecesaria.

## Use When
- Se ingiere material que proviene de fuera del repositorio (chats exportados, imagenes, capturas, MHTML, DOCX, volcados de datos, adjuntos).
- El cambio toca datos sensibles o integraciones (endpoints, cuentas, claves de servicios de terceros, informacion de personas).
- Se van a guardar derivados (resumenes, extractos, transcripciones, datasets) generados a partir de fuentes externas.

## Do Not Use When
- No hay material externo involucrado y el cambio no toca datos sensibles ni integraciones.
- El trabajo es puramente interno sobre artefactos ya redactados y verificados previamente.

## Read First
Revisar los documentos canonicos relevantes antes de proceder:
- `docs/CONTEXT_PACK.md` — contexto general del proyecto y convenciones vigentes.
- `docs/DECISION_LOG.md` — decisiones previas sobre manejo de datos sensibles e integraciones.
- `docs/MAINTENANCE_CHECKLIST.md` — pasos de mantenimiento y verificacion antes de versionar.
- `AGENTS.md` — reglas operativas y limites de actuacion de los agentes.

## Procedure
1. **Identificar** en el material entrante todo secreto o dato sensible: credenciales, tokens, cookies de sesion, claves de API, contraseñas, cadenas de conexion, y PII (nombres completos, documentos de identidad, correos, telefonos, direcciones, datos financieros o de salud).
2. **Redactar** cada elemento sensible antes de guardar cualquier derivado. Reemplazar el valor por un marcador neutro (por ejemplo `[REDACTADO]` o `[PII_REDACTADA]`) que preserve el contexto sin exponer el dato.
3. **No conservar** tokens, cookies, claves ni contraseñas en claro en ningun lugar: ni en el derivado, ni en notas de trabajo, ni en el historial de commits. Si un valor no es necesario para el proposito, eliminarlo por completo en vez de solo marcarlo.
4. **Reportar** los hallazgos y la remediacion aplicada: que tipos de secretos/PII se detectaron, donde, y como se redactaron o eliminaron. Dejar constancia sin repetir el valor sensible.

## Validation
- Ningun artefacto versionado contiene secretos (tokens, cookies, claves, contraseñas, cadenas de conexion) en claro.
- Ningun derivado conserva datos personales que no sean estrictamente necesarios para el proposito.
- Los marcadores de redaccion son consistentes y no filtran el valor original ni pistas para reconstruirlo.
- El reporte de hallazgos y remediacion existe y no reintroduce ningun secreto.

## Memory Update
- En `docs/`: si la ingesta genera una decision estable sobre manejo de datos sensibles o integraciones, registrarla en `docs/DECISION_LOG.md`; si cambia el contexto o las convenciones del proyecto, actualizar `docs/CONTEXT_PACK.md`; si aparece un paso de verificacion nuevo, reflejarlo en `docs/MAINTENANCE_CHECKLIST.md`.
- En el indice operacional: registrar la ejecucion concreta (que material se ingirio, cuando, y el resumen de remediacion) sin persistir ningun valor sensible. El indice operacional es efimero y de seguimiento; la fuente estable de decisiones permanece en `docs/`.

## Common Errors
- Guardar el material crudo sin redactar y planear "limpiarlo despues": una vez versionado, el secreto queda en el historial.
- Conservar credenciales, tokens o cookies en notas de trabajo, comentarios o mensajes de commit.
- Marcar el secreto como redactado pero dejar fragmentos suficientes para reconstruirlo.
