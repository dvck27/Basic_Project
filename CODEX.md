# CODEX.md — Adaptador para Codex

El contrato operativo primario es **[AGENTS.md](AGENTS.md)**. Léelo primero; esto solo añade recordatorios.

- La **capa portable multiagente** es `docs/agent_factory/` (agnóstica). Las skills canónicas están en
  `docs/agent_factory/skills/`; `.claude/` es solo espejo para Claude Code.
- La **verdad durable** vive en `docs/`; no dependas del historial de chat para la continuidad.
- **No importes** el stack ni las convenciones del repositorio guía: este repo es agnóstico (stack por definir).
- **Orden de lectura:** `README.md` → `docs/CONTEXT_PACK.md` → `docs/DECISION_LOG.md` → `docs/MAINTENANCE_CHECKLIST.md` → `specs/`/código.
