# GEMINI.md — Adaptador para Gemini / Antigravity

El contrato operativo primario es **[AGENTS.md](AGENTS.md)**. Léelo primero; esto solo añade recordatorios.

- La **capa portable multiagente** es `docs/agent_factory/` (no solo `.claude/`, que es específico de Claude Code).
  Usa las skills canónicas en `docs/agent_factory/skills/`.
- La **verdad durable** vive en `docs/`. El historial de chat es descartable; la continuidad está en los docs del repo.
- **No importes** asunciones del repositorio guía (stack, carpetas o herramientas): este repo es agnóstico.
- **Orden de lectura:** `README.md` → `docs/CONTEXT_PACK.md` → `docs/DECISION_LOG.md` → `docs/MAINTENANCE_CHECKLIST.md` → `specs/`/código.
