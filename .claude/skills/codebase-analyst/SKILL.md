---
name: codebase-analyst
description: Analiza arquitectura, dependencias, patrones y puntos criticos SIN modificar codigo, antes de un cambio mediano+, feature o refactor.
allowed-tools: Read, Grep, Glob, Bash
---

# codebase-analyst (wrapper Claude Code)

Skill de solo lectura: no edites ni ejecutes cambios de codigo.
Lee primero los canonicos: `docs/CONTEXT_PACK.md`, `docs/DECISION_LOG.md`, `docs/MAINTENANCE_CHECKLIST.md`, `AGENTS.md`.
Procedimiento: 1) mapea entrypoints, modulos y dependencias; 2) traza el flujo relevante a la tarea; 3) identifica tests existentes y riesgos estructurales; 4) reporta linaje e impacto.
Valida que el analisis permita planear el cambio con confianza y localizar los tests afectados. Si necesitas editar, cambia a la skill de implementacion.

> Fuente canonica: `docs/agent_factory/skills/codebase-analyst/SKILL.md`. `.claude/` es espejo, no fuente.
