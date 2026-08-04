---
name: memory-manager
description: Mantiene un indice operacional ligero para agentes con punteros a los docs canonicos, sin duplicar la verdad durable ni guardar secretos.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash
---

# memory-manager (wrapper Claude Code)

Manten un indice operacional ligero que acelere el trabajo repetido sin competir con `docs/`, que es la verdad durable.
Captura solo el hecho operacional y enlaza al doc canonico que posee el contexto (`docs/CONTEXT_PACK.md`, `docs/DECISION_LOG.md`).
Antes de crear una nota, busca duplicados y consolida en vez de acumular variantes casi identicas.
Nunca guardes secretos, credenciales ni datos personales: redactalos y apunta a donde se gestionan.
Si cambia contexto durable, actualiza primero `docs/` (CONTEXT_PACK y DECISION_LOG) y luego el puntero del indice.

> Fuente canonica: `docs/agent_factory/skills/memory-manager/SKILL.md`. `.claude/` es espejo, no fuente.
