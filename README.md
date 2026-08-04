# Basic_Project

Repositorio **base ("bootstrap") agent-ready**: un repo que parte vacío pero trae instalada, desde el inicio, una
**capa de operación por agentes de IA** (contratos multiagente, skills, memoria persistente, documentación viva,
PRPs y quality gates) adaptada de forma **agnóstica** (sin imponer ningún stack). Sirve como fundamento para
agregar código o clonarse a nuevos proyectos con la metodología ya montada.

> Principio de este README: **documenta solo lo verificable**. Lo que aún no existe se marca como `Por definir`.

## Estado del proyecto
- **Stack / lenguaje:** `Por definir` (agnóstico; todavía no hay código de aplicación).
- **Qué hay hoy:** la capa agent-ready (docs + contratos + skills) y el flujo de publicación a GitHub.
- **CI/CD, licencia, tests:** `Por definir`.

## Capa agent-ready
Cualquier agente (Claude, Gemini, Codex, Antigravity…) debe **empezar por [`AGENTS.md`](AGENTS.md)**.

- **[AGENTS.md](AGENTS.md)** — contrato operativo neutral (punto de entrada único).
- Adaptadores por proveedor: [`CLAUDE.md`](CLAUDE.md), [`GEMINI.md`](GEMINI.md), [`CODEX.md`](CODEX.md).
- **[docs/CONTEXT_PACK.md](docs/CONTEXT_PACK.md)** — continuidad entre sesiones.
- **[docs/DECISION_LOG.md](docs/DECISION_LOG.md)** — decisiones técnicas durables.
- **[docs/MAINTENANCE_CHECKLIST.md](docs/MAINTENANCE_CHECKLIST.md)** — qué mantener sincronizado.
- **[docs/agent_factory/](docs/agent_factory/)** — capa portable: 16 skills, PRPs, runbook, índice de memoria.
- **[docs/SAAS_FACTORY_ADOPTION_REPORT.md](docs/SAAS_FACTORY_ADOPTION_REPORT.md)** — qué se adoptó/adaptó/rechazó.

## Estructura del repositorio
```text
AGENTS.md, CLAUDE.md, GEMINI.md, CODEX.md   # contratos (entrada = AGENTS.md)
README.md                                    # este archivo
.gitignore                                   # incluye blindaje de secretos
docs/                                        # verdad durable, capa agent_factory y prompts .docx de referencia
.claude/                                     # espejo/adaptador para Claude Code (+ comando /subir)
```

## Publicar cambios
El repo se publica en GitHub (`https://github.com/dvck27/Basic_Project.git`, rama `main`). Formas de subir:

```bash
git add -A
git commit -m "mi mensaje"
git push origin main
```
- También puede usarse el comando **`/subir`** en Claude Code, que valida, crea el commit y ejecuta el push explícitamente.
- Detalles del remoto y autenticación: ver [docs/CONTEXT_PACK.md](docs/CONTEXT_PACK.md) → *Publicación y entorno*.
- **Nunca** guardes tokens/contraseñas en el repo (el `.gitignore` bloquea `Token_*.txt`, `*token*.txt`, `*.pat`, `.env`, `*.key`).

## Cómo empezar (agente o persona nueva)
1. Lee [`AGENTS.md`](AGENTS.md) y [`docs/CONTEXT_PACK.md`](docs/CONTEXT_PACK.md).
2. Revisa [`docs/DECISION_LOG.md`](docs/DECISION_LOG.md).
3. Usa la skill `repo-primer` (o `rescue-context` si perdiste el contexto).

## Límites conocidos
- Sin stack/código todavía: las skills dependientes de código son guía metodológica hasta que exista uno.
- Sin CI/CD ni licencia declarada — `Por definir`.
