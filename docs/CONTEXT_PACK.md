# Context Pack — Basic_Project

> Documento central de **continuidad**. Permite retomar el trabajo en un chat nuevo sin depender del historial.
> Regla: **solo lo verificable**; lo desconocido se marca `Por definir`.

## Qué es y qué problema resuelve
`Basic_Project` es un repositorio **base ("bootstrap") agent-ready**: parte de un repo vacío al que se le instaló
desde el inicio una **capa de operación por agentes de IA** (contratos, skills, memoria persistente, documentación
viva, PRPs y quality gates) adaptada de forma **agnóstica** del repo guía Orion. Sirve como plantilla/fundamento
para agregar código o clonarse a nuevos proyectos con la metodología ya montada.

- **Usuarios/casos:** el propietario de GitHub (`dvck27`) y cualquier agente de IA que opere el repo.
- **Estado actual:** solo la capa agent-ready + un `README` mínimo. **Aún no hay código de aplicación ni stack.**

## Arquitectura y stack
- **Stack:** `Por definir` (agnóstico). No se ha adoptado ningún lenguaje/framework todavía.
- **Arquitectura de la capa de agentes:**
  - Contratos raíz: `AGENTS.md` (entrada única) + adaptadores `CLAUDE.md`/`GEMINI.md`/`CODEX.md`.
  - Capa portable multiagente: `docs/agent_factory/` (skills, prps, runbooks, índice de memoria).
  - Espejo Claude Code: `.claude/` (wrappers de skills, memoria operacional, comandos).

## Jerarquía de fuentes de verdad
Código actual → specs/tests → **este Context Pack** → `README.md` → `DECISION_LOG.md` → memoria operacional
(`docs/agent_factory/memory/`, `.claude/memory/`) → repo guía/referencias → historial de chat (descartable).

## Separación de memoria (no confundir)
1. **Memoria runtime/operativa de una app** (JSON/JSONL, caches, logs, embeddings): pertenecería al futuro código; **no** es contexto de proyecto. *(Aún no existe.)*
2. **Memoria de contexto del proyecto** (durable, versionada): `docs/CONTEXT_PACK.md`, `docs/DECISION_LOG.md`, `docs/MAINTENANCE_CHECKLIST.md`, contratos raíz.
3. **Contratos técnicos**: `specs/` (cuando existan).
- Índice operacional de agentes: `docs/agent_factory/memory/` y `.claude/memory/` → **apuntan** a `docs/`, no la reemplazan. **Sin secretos ni perfiles personales.**

## Estructura del repositorio
```text
AGENTS.md, CLAUDE.md, GEMINI.md, CODEX.md   # contratos (entrada = AGENTS.md)
README.md                                    # onboarding
.gitignore                                   # incluye blindaje de secretos
docs/
  CONTEXT_PACK.md, DECISION_LOG.md, MAINTENANCE_CHECKLIST.md, SAAS_FACTORY_ADOPTION_REPORT.md
  agent_factory/  (README, memory/, prps/, runbooks/, skills/ = 16 skills)
  PROMPT_README_REPOSITORIOS.docx, PROMPT_MEMORIA_PERSISTENTE_REPOSITORIOS.docx  # prompts de referencia del usuario
.claude/
  commands/subir.md, memory/MEMORY.md, PRPs/, skills/ (wrappers)
```

## Publicación y entorno (durable)
Este repo se publica en **GitHub**: `https://github.com/dvck27/Basic_Project.git`, rama `main`.

- **Publicar:** comando `/subir` o secuencia explícita `git add -A`, `git commit` y `git push origin main`.
- **Remoto canónico:** `origin` apunta a GitHub y no se mantiene un remoto secundario.
- **Credenciales:** Git Credential Manager gestiona la autenticación HTTPS cuando sea necesaria. **Nunca** guardar
  tokens, contraseñas ni otras credenciales en el chat o en archivos versionados.
- **Identidad de commits:** configuración local del repositorio `Dave <dvck27@users.noreply.github.com>`.

## Comandos operativos
| Acción | Comando |
|---|---|
| Publicar cambios | `/subir` · o `git add -A` + `git commit` + `git push origin main` |
| Ver estado | `git status -s` · `git log --oneline` |
| Verificar remoto | `git ls-remote origin` |

*(No hay build/test/lint todavía: `Por definir` hasta que exista código.)*

## Cómo retomar en un chat nuevo
1. Lee `AGENTS.md`. 2. Lee este Context Pack. 3. Lee `DECISION_LOG.md` y `MAINTENANCE_CHECKLIST.md`.
4. Usa la skill `repo-primer` (o `rescue-context` si algo se perdió). 5. Revisa `git status` antes de cambiar nada.

## Riesgos / límites / deuda
- Repo sin código ni tests: las skills dependientes de código son guía metodológica hasta que exista stack.
- Sin CI/CD ni licencia declarada — `Por definir`.

## Qué actualizar cuando algo cambia
Ver `docs/MAINTENANCE_CHECKLIST.md`. Regla base: si cambia comportamiento → spec + tests; si cambia onboarding →
README; si cambia contexto durable → este Context Pack; si hay decisión durable → Decision Log.
