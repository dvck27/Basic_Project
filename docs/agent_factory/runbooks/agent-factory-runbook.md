# Agent Factory Runbook

Procedimiento reproducible de arranque y operación para cualquier agente.

## Start — Read Order
1. `AGENTS.md`
2. `README.md`
3. `docs/CONTEXT_PACK.md`
4. `docs/DECISION_LOG.md`
5. `docs/MAINTENANCE_CHECKLIST.md`
6. `specs/` y el código afectado (cuando existan)

## Operating Model
- Trata `docs/` como **verdad durable canónica**.
- Trata `docs/agent_factory/` como **capa portable multiagente** (skills/prps/runbooks/memoria).
- Trata `.claude/` como **espejo de compatibilidad** cuando el agente sea Claude Code.
- Usa el stack y los tests **reales del repo** (cuando existan); no importes asunciones del repo guía.
- Recupera contexto con `repo-primer`; si se perdió el hilo, `rescue-context`.

## Output Discipline
- Cambios mínimos y reversibles.
- Si cambia el comportamiento: actualiza spec, tests, README y Decision Log según corresponda.
- Redacta secretos y datos personales en cualquier artefacto derivado.
- Publica con el flujo del repo (`/subir` o `git add` + `git commit` + `git push origin main`).
