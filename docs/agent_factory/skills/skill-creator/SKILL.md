---
name: skill-creator
description: Crear o refinar skills reutilizables con el formato robusto del repositorio; usar cuando aparece un patron repetible o un workflow confuso que conviene estandarizar. Produce una skill canonica completa (y su wrapper .claude si aplica).
---

# Skill Creator

## Purpose
Estandarizar la creacion y el refinamiento de skills reutilizables dentro del repositorio, usando un formato robusto y verificable. El objetivo es que cualquier agente (humano o automatico) pueda ejecutar un procedimiento repetible sin depender de contexto de chat ni de conocimiento tacito. Evita las skills de una sola linea: una skill util documenta cuando aplicarse, que leer primero, como ejecutarse, como validarse y que dejar registrado.

## Use When
- Aparece un patron repetible: la misma secuencia de pasos se realiza mas de una vez y merece capturarse.
- Existe un workflow confuso o ambiguo que conviene estandarizar para reducir errores y variabilidad.
- Un procedimiento existente se explica cada vez de forma verbal y seria mejor tenerlo por escrito y reutilizable.
- Se quiere refinar una skill ya creada para que un segundo agente la use sin explicacion adicional.

## Do Not Use When
- El caso es unico y no se espera que se repita; documentarlo como skill agrega mantenimiento sin retorno.
- La tarea es una decision puntual o exploratoria sin procedimiento estable todavia (primero estabiliza el flujo, luego captura la skill).
- Ya existe una skill equivalente vigente; en ese caso refina la existente en lugar de crear una duplicada.

## Read First
Antes de crear o refinar una skill, revisa los documentos canonicos relevantes del repositorio:
- `AGENTS.md`: convenciones para agentes, alcance del repo y reglas de operacion base.
- `docs/CONTEXT_PACK.md`: contexto compartido y vocabulario del proyecto; asegura coherencia de nombres y supuestos.
- `docs/DECISION_LOG.md`: decisiones ya tomadas; evita contradecir acuerdos previos al definir el procedimiento.
- `docs/MAINTENANCE_CHECKLIST.md`: pasos de mantenimiento que la nueva skill debe respetar o referenciar.
- Skills existentes en `docs/agent_factory/skills/` para reutilizar formato y evitar duplicados.

## Procedure
1. **Mantener la skill acotada.** Define un unico proposito claro y un alcance estrecho. Si el procedimiento cubre varios objetivos distintos, separalo en skills independientes. Evita las skills de una sola linea: cada skill debe ser autosuficiente y accionable.
2. **Incluir todas las secciones del formato robusto.** La skill canonica debe contener, en este orden: `Purpose`, `Use When`, `Do Not Use When`, `Read First`, `Procedure`, `Validation` y `Memory Update`. Agrega `Common Errors` solo cuando aporte valor (fallos frecuentes y como evitarlos). Redacta cada seccion de forma concreta y accionable, sin ambiguedad.
3. **Preferir docs repo-local sobre memoria de chat.** Referencia y actualiza documentos versionados del repositorio (por ejemplo los de `docs/`) en lugar de apoyarte en contexto de conversacion, que no persiste ni es auditable. Toda informacion que la skill necesite debe poder recuperarse desde el repositorio.
4. **Crear el wrapper `.claude` si aplica.** Si la skill se usara desde el entorno Claude, crea un wrapper fino en `.claude/skills/<name>/SKILL.md` que apunte a la fuente canonica. El wrapper es un espejo delgado, no la fuente de verdad: la fuente canonica siempre vive en `docs/agent_factory/skills/<name>/SKILL.md`.
5. **Mantener la neutralidad de stack.** No asumas lenguaje, framework ni herramientas concretas. No inventes comandos ni rutas que no existan. No incluyas secretos, credenciales ni datos sensibles.

## Validation
La skill esta lista cuando un segundo agente puede ejecutarla de principio a fin sin explicacion extra, apoyandose solo en el texto de la skill y en los documentos que esta referencia. Verifica que:
- Cada seccion del formato robusto esta presente y es accionable.
- `Read First` referencia documentos que existen y son pertinentes.
- El procedimiento no depende de contexto de chat ni de conocimiento tacito.
- No hay comandos inventados, secretos ni supuestos de stack.
- Si existe wrapper `.claude`, este apunta correctamente a la fuente canonica.

## Memory Update
- **En `docs/`:** consolida el conocimiento duradero. Si la skill introduce o formaliza una decision, registrala en `docs/DECISION_LOG.md`. Si afecta el contexto compartido, actualiza `docs/CONTEXT_PACK.md`. Si agrega o cambia un paso recurrente de mantenimiento, refleja el cambio en `docs/MAINTENANCE_CHECKLIST.md`. La skill canonica en `docs/agent_factory/skills/<name>/SKILL.md` es la fuente de verdad.
- **En el indice operacional:** registra la existencia de la skill (nombre, ubicacion y proposito) en el listado o indice operativo del repositorio para que sea descubrible, y crea o actualiza el espejo en `.claude/skills/<name>/SKILL.md` si aplica. El indice operacional apunta a la fuente canonica; no la reemplaza ni la duplica.

## Common Errors
- **Skill de una sola linea:** describe el resultado deseado pero no el procedimiento; un segundo agente no puede ejecutarla. Completa todas las secciones.
- **Dependencia de memoria de chat:** la skill referencia contexto que no existe en el repositorio. Muevelo a `docs/` y referencia la ruta.
- **Alcance demasiado amplio:** una sola skill intenta cubrir varios objetivos. Divide en skills acotadas.
- **Wrapper como fuente de verdad:** editar la logica en `.claude/` en lugar de la canonica. Mantén `.claude/` como espejo fino.
- **Supuestos de stack o comandos inventados:** rompen la agnosticidad. Mantén el procedimiento neutral y verificable.
