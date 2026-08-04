---
name: prp
description: Exige una propuesta tecnica (PRP) antes de un cambio grande y produce un documento completo, basado en el codigo real, que otro agente pueda implementar sin preguntar.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash
---

# prp (wrapper Claude Code)

Antes de un cambio grande (arquitectura, subsistemas, migraciones de carpetas, flujo de agentes, persistencia, seguridad, testing o adopcion amplia de patrones), exige un PRP; para un fix pequeño usa sprint.
Lee primero `docs/CONTEXT_PACK.md`, `docs/DECISION_LOG.md`, `docs/MAINTENANCE_CHECKLIST.md` y `AGENTS.md`.
Copia la plantilla `docs/agent_factory/prps/prp-base.md` a un archivo nuevo y completa: Problem, Objective, Current Context, Scope, Out of Scope, Proposed Design, Affected Files, Risks, Validation, Rollback Plan y Acceptance Criteria, basandote en el codigo real y sin adivinanzas.
El PRP esta listo cuando otro agente puede implementarlo sin preguntar; luego actualiza `docs/` y el indice operacional segun corresponda.

> Fuente canonica: `docs/agent_factory/skills/prp/SKILL.md`. `.claude/` es espejo, no fuente.
