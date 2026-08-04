# Agent Factory — capa portable multiagente

Capa **canónica y agnóstica** de operación por agentes. Portable a cualquier repositorio y cualquier agente
(Claude, Gemini, Codex, Antigravity u otro).

## Reglas canónicas
- `docs/` es la **verdad durable** del proyecto.
- `AGENTS.md` (raíz) es el **punto de entrada** de todo agente.
- `docs/agent_factory/` es la **capa portable**: skills, PRPs, runbooks e índice de memoria operacional.
- `.claude/` es un **espejo/adaptador** para Claude Code, **no** una fuente de verdad.
- **Sin secretos** en ningún archivo. Separar memoria runtime de memoria de proyecto.

## Contenido
- `skills/` — 16 skills reutilizables (ver `skills/SKILLS_README.md`).
- `prps/prp-base.md` — plantilla de propuesta para cambios grandes.
- `runbooks/agent-factory-runbook.md` — procedimiento de arranque y modelo de operación.
- `memory/README.md` — reglas del índice de memoria operacional.

## Cómo usar
1. Empieza por `AGENTS.md` → `docs/CONTEXT_PACK.md`.
2. Ejecuta la skill `repo-primer` para recuperar contexto.
3. Aplica la skill adecuada según la tarea (fix pequeño → `sprint`; cambio grande → `prp` + `phased-implementation`).
4. Al terminar, sincroniza docs/tests (skill `documentation-sync`, ver `docs/MAINTENANCE_CHECKLIST.md`).
