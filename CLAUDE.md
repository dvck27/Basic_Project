# CLAUDE.md — Adaptador para Claude Code

El contrato operativo primario es **[AGENTS.md](AGENTS.md)**. Léelo primero; esto solo añade matices de Claude Code.

- **Fuente canónica de skills:** `docs/agent_factory/skills/` (agnóstica). `.claude/skills/` son *wrappers* de
  compatibilidad que añaden `allowed-tools`; **no** son la fuente de verdad.
- **Memoria:** la verdad durable vive en `docs/`. `.claude/memory/MEMORY.md` es solo un índice operacional que
  apunta a `docs/`. No dupliques docs en la memoria ni guardes secretos.
- **Orden de lectura:** el mismo de AGENTS.md → `README.md` → `docs/CONTEXT_PACK.md` → `docs/DECISION_LOG.md` →
  `docs/MAINTENANCE_CHECKLIST.md` → `specs/`/código.

## Publicar cambios
El comando **`/subir`** valida los cambios, crea el commit y ejecuta un push explícito a GitHub (`origin/main`).
También puede usarse `git add` + `git commit` + `git push origin main`. Detalles del remoto y autenticación:
`docs/CONTEXT_PACK.md` → *Publicación y entorno*. **Nunca** pegues tokens/contraseñas en el chat.
