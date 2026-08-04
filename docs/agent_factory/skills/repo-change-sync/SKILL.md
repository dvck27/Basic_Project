---
name: repo-change-sync
description: Sincroniza el espejo .claude/ con la fuente canonica docs/agent_factory/ cuando ambas capas divergen; produce wrappers finos regenerados que apuntan al canonico.
---

# Sincronizacion de cambios entre capa canonica y espejo Claude

## Purpose
Mantener el espejo `.claude/` alineado con la fuente unica de verdad ubicada en
`docs/agent_factory/`. La capa canonica define el contenido real de skills y PRPs;
`.claude/` es solo un espejo operativo de wrappers finos que Claude Code consume.
Esta skill detecta divergencias y regenera los wrappers para que nunca contradigan
ni dupliquen contenido canonico.

## Use When
- `.claude/` divergio de `docs/agent_factory/` (por ejemplo, skills o PRPs cambiaron
  en la capa canonica pero el wrapper quedo desactualizado).
- Se agrego una skill o PRP nuevo en `docs/agent_factory/` y falta su wrapper espejo.
- Un wrapper en `.claude/` describe un procedimiento distinto al del canonico.
- Se necesita verificar que cada wrapper apunta correctamente a su skill canonica.

## Do Not Use When
- No hubo cambios en la capa canonica `docs/agent_factory/` desde la ultima
  sincronizacion.
- Se pretende agregar contenido funcional nuevo: eso debe crearse primero en el
  canonico, no en el espejo.
- El cambio pertenece a documentacion de proyecto (docs/ raiz) sin relacion con
  skills o PRPs.

## Read First
Antes de sincronizar, revisa los documentos canonicos relevantes para entender
convenciones y contexto vigente:
- `docs/CONTEXT_PACK.md` — contexto operativo y convenciones del repositorio.
- `docs/DECISION_LOG.md` — decisiones previas que fijan estructura y reglas de las capas.
- `docs/MAINTENANCE_CHECKLIST.md` — pasos de mantenimiento y verificacion periodica.
- `AGENTS.md` — reglas para agentes y limites de cada capa.
- La skill canonica objetivo en `docs/agent_factory/skills/<name>/SKILL.md` y su
  wrapper espejo en `.claude/skills/<name>/SKILL.md`.

## Procedure
1. Comparar canonico vs wrapper.
   - Listar las skills en `docs/agent_factory/skills/` y sus wrappers en
     `.claude/skills/`.
   - Para cada `<name>`, comparar el frontmatter (name, description) del canonico
     con el del wrapper y detectar diferencias, ausencias o contradicciones.
2. Regenerar el wrapper fino.
   - Reescribir `.claude/skills/<name>/SKILL.md` como wrapper fino: frontmatter
     (name, description alineada al canonico, allowed-tools) mas 3-6 lineas con lo
     esencial del procedimiento.
   - Incluir un puntero explicito a la skill canonica
     `docs/agent_factory/skills/<name>/SKILL.md` y una linea que aclare que
     `.claude/` es espejo, no fuente.
3. Verificar la fuente unica.
   - Confirmar que todo el contenido de detalle sigue viviendo en el canonico y que
     el wrapper solo resume y referencia.
4. No introducir contenido nuevo solo en el espejo.
   - Si al comparar surge la necesidad de detalle adicional, agregarlo primero en el
     canonico y luego reflejar el resumen en el wrapper. Nunca al reves.

## Validation
- Cada wrapper `.claude/skills/<name>/SKILL.md` existe y su `name` coincide con el
  canonico correspondiente.
- Cada wrapper contiene un puntero a `docs/agent_factory/skills/<name>/SKILL.md`.
- El wrapper no contradice ni duplica el contenido detallado del canonico.
- No queda ninguna skill canonica sin wrapper, ni ningun wrapper huerfano sin
  canonico.
- El frontmatter del wrapper esta bien formado (name y description presentes,
  allowed-tools declarado).

## Memory Update
- En `docs/`: si la sincronizacion revela una decision estructural (por ejemplo,
  como se generan los wrappers o que capa manda), registrala en
  `docs/DECISION_LOG.md`; si cambia un paso recurrente de mantenimiento, actualiza
  `docs/MAINTENANCE_CHECKLIST.md`; si cambia contexto o convenciones, ajusta
  `docs/CONTEXT_PACK.md`.
- En el indice operacional: actualiza el listado de skills/wrappers vigentes para
  reflejar altas, bajas o renombrados, de modo que el espejo `.claude/` quede
  documentado como derivado del canonico.

## Common Errors
- Editar el wrapper en `.claude/` en lugar del canonico: el cambio se pierde en la
  siguiente regeneracion. Corrige siempre primero en `docs/agent_factory/`.
- Copiar el contenido completo del canonico dentro del wrapper: rompe el principio
  de fuente unica y genera divergencia futura. El wrapper debe permanecer fino.
- Dejar un wrapper sin puntero al canonico o con un `name` que no coincide.
