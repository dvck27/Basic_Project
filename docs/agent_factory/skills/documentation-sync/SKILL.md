---
name: documentation-sync
description: Usala cuando un cambio altere el comportamiento observable, el onboarding, la arquitectura o una politica, para mantener la documentacion alineada con el codigo real y evitar divergencia.
---

# Documentation Sync

## Purpose
Prevenir la divergencia entre el codigo y la documentacion cuando cambia el comportamiento del sistema. Cada vez que una modificacion altera lo que otra persona o agente observa, la documentacion canonica debe reflejarlo de forma minima, coherente y sin contradicciones. El objetivo no es reescribir docs completos, sino cerrar la brecha exacta que abrio el cambio y dejar declarados los huecos que queden pendientes.

## Use When
Aplica esta skill cuando el cambio produce un efecto observable, por ejemplo:
- Cambia el **comportamiento** visible del sistema (entradas, salidas, flujos, mensajes, resultados, contratos).
- Cambia el **onboarding** o la forma de arrancar, configurar o usar el proyecto.
- Cambia la **arquitectura**: componentes, limites, dependencias, integraciones o responsabilidades.
- Cambia una **politica**: convenciones, reglas de decision, criterios de calidad, seguridad o gobernanza.

## Do Not Use When
- El cambio es **puramente interno y sin efecto observable** (refactor equivalente, renombrado local, formato, comentarios) que no altera comportamiento, onboarding, arquitectura ni politica.
- El cambio ya esta cubierto por documentacion vigente y correcta; no hay brecha que cerrar.
- El cambio es un experimento descartado o revertido que nunca llego a afectar el comportamiento del sistema.

## Read First
Antes de tocar nada, lee los documentos canonicos relevantes para conocer el estado declarado y no duplicar ni contradecir:
- `AGENTS.md` — reglas de operacion y convenciones para agentes y colaboradores.
- `docs/CONTEXT_PACK.md` — contexto general del proyecto, arquitectura y estado actual.
- `docs/DECISION_LOG.md` — decisiones tomadas y su justificacion; verifica si el cambio deriva de o afecta una decision registrada.
- `docs/MAINTENANCE_CHECKLIST.md` — lista de verificacion de mantenimiento; es la referencia operativa de esta skill.
- `README.md` — descripcion de entrada, uso y onboarding del repositorio.
- Cualquier `spec` o documento de diseño asociado al area que cambio.

## Procedure
1. **Identificar los docs desalineados.** Compara el comportamiento real (tras el cambio) contra lo que declaran los documentos. Recorre al menos `README.md`, `docs/CONTEXT_PACK.md`, `docs/DECISION_LOG.md` y los `specs` del area. Anota que afirmacion quedo obsoleta o incompleta en cada uno.
2. **Actualizar de forma minima y coherente.** Modifica solo lo necesario para que cada documento describa el comportamiento actual. Usa el mismo vocabulario y las mismas rutas que el resto de la documentacion. No agregues detalle especulativo ni reescribas secciones que no cambiaron.
3. **Verificar la ausencia de contradicciones.** Relee los documentos actualizados en conjunto y confirma que no se contradigan entre si ni con los documentos canonicos que no editaste. Resuelve conflictos dejando una sola fuente de verdad por afirmacion.
4. **Declarar los gaps pendientes.** Si queda documentacion desalineada que no se puede cerrar ahora (falta contexto, decision no tomada, area fuera de alcance), registra explicitamente el hueco pendiente en el documento adecuado (por ejemplo una nota en `docs/CONTEXT_PACK.md` o una entrada en `docs/DECISION_LOG.md`) para que no se pierda.

## Validation
La skill se considera completa cuando:
- `README.md` coincide con el comportamiento y el onboarding reales.
- `docs/CONTEXT_PACK.md` refleja la arquitectura y el estado actuales.
- `docs/DECISION_LOG.md` recoge las decisiones que motivaron o resultaron del cambio.
- Los `specs` describen el comportamiento tal como es hoy.
- No existen contradicciones entre estos documentos ni con los demas docs canonicos.
- Los gaps que no se cerraron quedan declarados de forma visible.
- Se recorrio `docs/MAINTENANCE_CHECKLIST.md` como referencia de cierre.

## Memory Update
- **En `docs/` (fuente de verdad):** actualiza el contenido canonico que describe el comportamiento del sistema — `README.md`, `docs/CONTEXT_PACK.md`, `docs/DECISION_LOG.md`, `specs` y, cuando aplique, `AGENTS.md`. Estos documentos son la memoria persistente y autoritativa del proyecto.
- **En el indice operacional:** registra unicamente el rastro de esta ejecucion (que docs se tocaron, que gaps quedaron pendientes, cuando se sincronizo). El indice operacional apunta a los documentos canonicos; no duplica su contenido ni se convierte en fuente alternativa de verdad.

## Common Errors
- **Actualizar solo un documento** y dejar los demas desalineados, generando contradicciones entre `README.md`, `docs/CONTEXT_PACK.md`, `docs/DECISION_LOG.md` y `specs`.
- **Reescribir de mas:** cambiar secciones no afectadas introduce ruido y riesgo de nuevos errores; mantente en el cambio minimo.
- **Duplicar la verdad:** copiar el mismo detalle en varios lugares crea futuras divergencias; deja una sola fuente por afirmacion y referencia desde el resto.
- **Omitir la declaracion de gaps:** dejar huecos sin registrar hace que la divergencia reaparezca mas adelante.
