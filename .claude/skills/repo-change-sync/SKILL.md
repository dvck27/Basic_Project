---
name: repo-change-sync
description: Regenera los wrappers finos de .claude/ para mantenerlos sincronizados con la fuente canonica docs/agent_factory/ cuando ambas capas divergen.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash
---

# repo-change-sync (wrapper Claude Code)

Usar cuando `.claude/` divergio de `docs/agent_factory/` (skills o PRPs). Comparar
el canonico con su wrapper por `<name>`, luego regenerar cada wrapper fino
(frontmatter con name/description/allowed-tools mas puntero al canonico). No
introducir contenido nuevo solo en el espejo: todo detalle vive en el canonico y el
wrapper solo resume y referencia. Verificar que cada wrapper apunta a su skill
canonica y no la contradice.

> Fuente canonica: `docs/agent_factory/skills/repo-change-sync/SKILL.md`. `.claude/` es espejo, no fuente.
