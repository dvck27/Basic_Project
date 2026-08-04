---
name: context-pack-maintainer
description: Manten docs/CONTEXT_PACK.md compacto y exacto cuando cambie algo duradero (proposito, arquitectura, entrypoints, memoria, dependencias, publicacion o riesgos) para retomar en un chat nuevo.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash
---

# context-pack-maintainer (wrapper Claude Code)

Usala cuando cambie un hecho duradero del proyecto: proposito, arquitectura, entrypoints, estructura, modelo de memoria, orden de lectura, dependencias criticas, configuracion durable, flujo de publicacion o riesgos. No la uses para estado efimero o memoria runtime.
Procedimiento: 1) verifica el estado real del repositorio; 2) actualiza solo las secciones afectadas de `docs/CONTEXT_PACK.md`, manteniendolo compacto; 3) conserva la jerarquia de fuentes de verdad y el "como retomar en un chat nuevo"; 4) declara los gaps en vez de inventar.
Lee primero `docs/CONTEXT_PACK.md`, `AGENTS.md`, `docs/DECISION_LOG.md` y `docs/MAINTENANCE_CHECKLIST.md`. Valida que un agente nuevo pueda retomar leyendo el Context Pack sin adivinar.

> Fuente canonica: `docs/agent_factory/skills/context-pack-maintainer/SKILL.md`. `.claude/` es espejo, no fuente.
