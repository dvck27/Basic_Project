---
name: rescue-context
description: Reconstruye el estado del proyecto cuando se pierde el chat o hay drift entre fuentes; produce un bloque "Estado Recuperado" para continuar sin el historial.
---

# Rescue Context

## Purpose
Recuperar el estado operativo del proyecto cuando la conversacion se perdio, la
memoria o los documentos estan dañados, o existe drift (desalineacion) entre las
fuentes persistentes. El resultado es un bloque compacto llamado "Estado
Recuperado" que permite retomar el trabajo apoyandose unicamente en los
artefactos versionados del repositorio, sin depender del historial del chat.

## Use When
- Se perdio la conversacion o el hilo de trabajo y no hay contexto en memoria.
- Los documentos persistentes o la memoria operativa estan dañados, truncados o
  contradictorios.
- Hay amnesia de estado: no se sabe cual es el objetivo actual, que se hizo, ni
  cuales son los proximos pasos.
- Se detecta drift entre lo que dicen los documentos canonicos y lo que muestra
  el estado real del repositorio.

## Do Not Use When
- El contexto de trabajo esta intacto y solo se necesita orientacion inicial: en
  ese caso usa la skill `repo-primer`.
- Solo se requiere una tarea puntual bien definida con todo el contexto ya
  presente; no hace falta reconstruir estado.

## Read First
Lee estos documentos canonicos en orden. Todas las rutas son relativas a la raiz
del repositorio.

1. `AGENTS.md` — reglas de operacion, convenciones y como debe trabajar un agente
   en este repositorio.
2. `docs/CONTEXT_PACK.md` — objetivo del proyecto, alcance, estado y contexto de
   alto nivel.
3. `docs/DECISION_LOG.md` — decisiones tomadas y su justificacion; util para
   entender por que las cosas estan como estan.
4. `docs/MAINTENANCE_CHECKLIST.md` — tareas de mantenimiento pendientes y estado
   de salud del proyecto.

## Procedure
1. **Leer los documentos persistentes en orden.** Recorre `AGENTS.md`,
   `docs/CONTEXT_PACK.md`, `docs/DECISION_LOG.md` y
   `docs/MAINTENANCE_CHECKLIST.md`. Anota objetivo declarado, decisiones vigentes,
   restricciones y pendientes. Marca cualquier inconsistencia entre documentos.
2. **Inspeccionar el estado del repositorio con git.** Revisa el historial
   reciente y el estado del arbol de trabajo (por ejemplo, el registro de commits
   recientes y los archivos modificados/sin seguimiento). Contrasta lo que el
   repositorio muestra con lo que los documentos afirman, para detectar drift.
3. **Reconstruir objetivo, estado y proximos pasos.** A partir de documentos y
   git, sintetiza: cual es el objetivo actual, en que punto esta el trabajo, que
   se completo, que quedo a medias y cuales son los siguientes pasos logicos.
4. **Producir el bloque "Estado Recuperado".** Redacta un resumen compacto y
   accionable con la estructura de abajo. Debe bastar por si solo para continuar
   sin el historial del chat.

Formato sugerido del bloque:

```markdown
## Estado Recuperado

- **Objetivo:** <objetivo actual del proyecto o de la tarea>
- **Estado:** <en que punto esta el trabajo; que esta completo y que a medias>
- **Fuentes usadas:** <documentos y señales de git consultados>
- **Drift detectado:** <inconsistencias entre docs y repositorio, o "ninguno">
- **Proximos pasos:** <lista corta y priorizada de acciones concretas>
- **Riesgos / dudas:** <supuestos, huecos de informacion o preguntas abiertas>
```

## Validation
- El bloque "Estado Recuperado" permite continuar el trabajo sin el historial del
  chat.
- El objetivo, el estado y los proximos pasos son coherentes entre si y con lo que
  muestran los documentos canonicos y el estado del repositorio.
- Cualquier drift detectado queda registrado explicitamente en el bloque.
- No se inventaron hechos: cada afirmacion se apoya en un documento persistente o
  en una señal verificable del repositorio.

## Memory Update
- **En `docs/` (fuente canonica):** si al recuperar el estado se descubren
  desalineaciones reales, corrige el documento correspondiente. Actualiza
  `docs/CONTEXT_PACK.md` cuando cambie el objetivo o el estado; añade una entrada
  en `docs/DECISION_LOG.md` si se toma o se aclara una decision; ajusta
  `docs/MAINTENANCE_CHECKLIST.md` si aparecen o se cierran pendientes.
- **En el indice operacional (memoria de trabajo):** registra el bloque "Estado
  Recuperado" como punto de partida de la sesion. Este indice es efimero y refleja
  el estado de trabajo actual; no reemplaza a los documentos canonicos, que son la
  unica fuente de verdad persistente.

## Common Errors
- Producir el bloque solo con documentos sin contrastar contra git (o viceversa):
  se pierde la deteccion de drift. Usa ambas fuentes.
- Confundir el indice operacional con la fuente canonica: los cambios de estado
  duraderos van a `docs/`, no solo a la memoria de trabajo.
- Rellenar huecos con suposiciones no verificadas. Si un dato falta, decláralo en
  "Riesgos / dudas" en lugar de inventarlo.
