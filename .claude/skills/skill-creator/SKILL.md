---
name: skill-creator
description: Crear o refinar skills reutilizables con formato robusto cuando aparece un patron repetible o un workflow confuso; produce una skill canonica completa y su wrapper.
allowed-tools: Read, Write, Edit, Glob, Grep
---

# skill-creator (wrapper Claude Code)

Usa esta skill cuando detectes un patron repetible o un workflow confuso que convenga estandarizar; evita skills de una sola linea.
Manten la skill acotada e incluye siempre: Purpose, Use When, Do Not Use When, Read First, Procedure, Validation y Memory Update.
Antes de escribir, revisa `AGENTS.md`, `docs/CONTEXT_PACK.md`, `docs/DECISION_LOG.md` y `docs/MAINTENANCE_CHECKLIST.md`, y reutiliza el formato de `docs/agent_factory/skills/`.
Prefiere documentos repo-local sobre memoria de chat; no asumas stack, no inventes comandos y no incluyas secretos.
Valida que un segundo agente pueda usar la skill sin explicacion extra, y crea este wrapper `.claude` solo como espejo fino.

> Fuente canonica: `docs/agent_factory/skills/skill-creator/SKILL.md`. `.claude/` es espejo, no fuente.
