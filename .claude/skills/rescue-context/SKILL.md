---
name: rescue-context
description: Reconstruye el estado del proyecto cuando se pierde el chat o hay drift entre fuentes; produce un bloque "Estado Recuperado".
allowed-tools: Read, Grep, Glob, Bash
---

# rescue-context (wrapper Claude Code)

Usa esta skill cuando se perdio la conversacion, los docs/memoria estan dañados o hay drift entre fuentes.

1. Lee en orden los docs persistentes: `AGENTS.md`, `docs/CONTEXT_PACK.md`, `docs/DECISION_LOG.md`, `docs/MAINTENANCE_CHECKLIST.md`.
2. Inspecciona el repositorio con git (log reciente y estado del arbol) y contrasta contra los docs para detectar drift.
3. Reconstruye objetivo, estado y proximos pasos, y produce un bloque compacto "Estado Recuperado" que permita continuar sin el historial del chat.

> Fuente canonica: `docs/agent_factory/skills/rescue-context/SKILL.md`. `.claude/` es espejo, no fuente.
