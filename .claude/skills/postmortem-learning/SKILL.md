---
name: postmortem-learning
description: Convierte un fallo o incidente en un control de ingenieria durable (regla + test de regresion + docs sincronizados).
allowed-tools: Read, Write, Edit, Grep, Glob, Bash
---

# postmortem-learning (wrapper Claude Code)

Usala cuando un fix se repite, un workflow confunde o un fallo deberia volverse regla. No la uses si el evento es trivial o el material tiene secretos sin redactar.

Procedimiento esencial: declara sintoma e impacto; arma una linea de tiempo factual (comandos, logs, diffs); separa hechos, hipotesis descartadas e incertidumbre; identifica causa raiz y contribuyentes; define una regla de prevencion; agrega un test de regresion que no mute el estado real del usuario; sincroniza docs (spec, runbook, `docs/CONTEXT_PACK.md`, `docs/DECISION_LOG.md`) y guarda el reporte en `docs/`.

Valida que el fallo se reconozca de forma determinista, que el fix sea reproducible y que los docs coincidan con el comportamiento real.

> Fuente canonica: `docs/agent_factory/skills/postmortem-learning/SKILL.md`. `.claude/` es espejo, no fuente.
