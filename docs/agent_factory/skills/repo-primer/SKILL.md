---
name: repo-primer
description: Al iniciar o retomar una sesion, reconstruye el modelo mental del repositorio desde fuentes repo-local y produce un resumen operativo compacto y accionable.
---

# Repo Primer

## Purpose
Recuperar el modelo mental del repositorio desde fuentes repo-local (no desde la memoria del chat) al comenzar a trabajar, y producir un resumen operativo compacto que permita continuar de forma segura. El resultado es un briefing corto y verificable que cualquier agente puede usar como punto de partida, sin depender del historial de la conversacion.

## Use When
- Se inicia un chat nuevo sin contexto previo cargado.
- Se retoma trabajo previo despues de una pausa, un cambio de sesion o un traspaso entre agentes.
- Antes de emprender un cambio mediano o grande (nueva funcionalidad, refactor, cambio estructural, decision de diseno).
- Cuando hay dudas sobre el objetivo actual, el estado del repo o las decisiones ya tomadas.

## Do Not Use When
- Correcciones triviales de una sola linea (typo, ajuste de formato, cambio evidente y aislado).
- Ya se cargo y validado el modelo mental en la misma sesion y el contexto sigue vigente.
- La tarea no toca el repositorio (consulta puramente externa o conversacional).

## Read First
Lee los documentos canonicos en este orden. Todas las rutas son relativas a la raiz del repositorio:
1. `AGENTS.md` — reglas operativas para agentes, convenciones y limites de actuacion.
2. `docs/CONTEXT_PACK.md` — objetivo del proyecto, alcance, estado actual y contexto durable.
3. `docs/DECISION_LOG.md` — decisiones tomadas, su justificacion y las alternativas descartadas.
4. `docs/MAINTENANCE_CHECKLIST.md` — tareas de mantenimiento, invariantes y verificaciones recurrentes.

Estos son la fuente de verdad. Si alguno no existe o esta desactualizado, registralo como hallazgo en el resumen en lugar de asumir su contenido.

## Procedure
1. **Identificar el objetivo actual.** Determina que se pide en esta sesion (peticion del usuario o tarea pendiente). Enuncialo en una frase antes de leer nada mas, para orientar la lectura.
2. **Leer los docs canonicos en orden.** Recorre `AGENTS.md`, luego `docs/CONTEXT_PACK.md`, `docs/DECISION_LOG.md` y `docs/MAINTENANCE_CHECKLIST.md`. Extrae solo lo relevante al objetivo: reglas que apliquen, estado vigente, decisiones que condicionan el cambio y verificaciones exigidas.
3. **Inspeccionar el area de la tarea.** Revisa el estado del arbol de trabajo (`git status`) y localiza los archivos y directorios que la tarea probablemente tocara. Abre los relevantes para confirmar su estructura real; no infieras stack ni convenciones — verificalas en los archivos.
4. **Producir el resumen operativo.** Entrega un briefing compacto con estos cinco puntos:
   - **Objetivo del proyecto:** que es y para que existe (segun `CONTEXT_PACK`).
   - **Estado actual:** donde esta el trabajo hoy, incluyendo cambios sin confirmar detectados en `git status`.
   - **Docs durables:** documentos y decisiones canonicas que condicionan la tarea, citados por ruta.
   - **Archivos afectados:** que se tocara o revisara para cumplir el objetivo.
   - **Proximo paso seguro:** la accion inmediata mas prudente y de menor riesgo para avanzar.

## Validation
El resumen esta bien hecho si un segundo agente, sin acceso al historial de este chat, puede continuar el trabajo leyendo solo ese resumen y los docs citados. Verifica que: el objetivo esta enunciado con claridad, cada afirmacion sobre el estado o las decisiones remite a una fuente repo-local, no se asume ningun stack ni comando no confirmado, y el proximo paso es concreto y accionable.

## Memory Update
- **Actualizar en `docs/` (memoria durable):** si durante la sesion cambia el alcance u objetivo, se toma una decision de diseno o se descarta una alternativa, o cambia una invariante de mantenimiento. Registra objetivo/estado en `docs/CONTEXT_PACK.md`, decisiones y su justificacion en `docs/DECISION_LOG.md`, y verificaciones o invariantes en `docs/MAINTENANCE_CHECKLIST.md`.
- **Actualizar en el indice operacional (memoria efimera de sesion):** el progreso momentaneo, los archivos abiertos, los siguientes pasos inmediatos y las notas de trabajo que no son durables. Esto orienta la sesion en curso pero no pertenece a los docs canonicos.
- **Regla:** lo que otro agente necesitaria para continuar va a `docs/`; lo que solo sirve para el hilo actual se queda en el indice operacional.

## Common Errors
- Reconstruir el contexto desde la memoria del chat en lugar de leer las fuentes repo-local; el resumen deja de ser reproducible.
- Asumir lenguaje, framework o comandos no confirmados; este repositorio es agnostico y el stack debe verificarse en los archivos.
- Omitir `git status` y perderse cambios sin confirmar, describiendo un estado que no coincide con el arbol de trabajo.
- Volcar los docs completos en el resumen en vez de extraer solo lo relevante al objetivo.
