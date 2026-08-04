---
name: sprint
description: Fix pequeño, acotado y de bajo riesgo con ceremonia mínima; cambio localizado validado sin efectos colaterales.
allowed-tools: Read, Grep, Glob, Bash
---

# sprint (wrapper Claude Code)

Usa esta skill solo si el fix es localizado, no toca arquitectura ni cruza módulos y no requiere PRP. Si crece o es transversal, escala a `prp` + `phased-implementation`.

Procedimiento: 1) confirma el alcance mínimo, 2) aplica el cambio mínimo sin refactorizar de paso, 3) valida con la comprobación más pequeña que ya exista para esa área, 4) actualiza `docs/` solo si cambió el uso o el onboarding.

Antes de tocar código, lee los canónicos relevantes: `docs/CONTEXT_PACK.md`, `docs/DECISION_LOG.md`, `docs/MAINTENANCE_CHECKLIST.md`, `AGENTS.md`.

> Fuente canónica: `docs/agent_factory/skills/sprint/SKILL.md`. `.claude/` es espejo, no fuente.
