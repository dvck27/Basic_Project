---
name: documentation-sync
description: Manten la documentacion alineada con el codigo real cuando un cambio altere comportamiento, onboarding, arquitectura o politica.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash
---

# documentation-sync (wrapper Claude Code)

Usala cuando un cambio produzca un efecto observable (comportamiento, onboarding, arquitectura o politica). No la uses en cambios puramente internos sin efecto observable.

Procedimiento breve: 1) identifica los docs desalineados (`README.md`, `docs/CONTEXT_PACK.md`, `docs/DECISION_LOG.md`, `specs`); 2) actualizalos de forma minima y coherente; 3) verifica que no se contradigan entre si; 4) declara los gaps pendientes. Referencia de cierre: `docs/MAINTENANCE_CHECKLIST.md`.

> Fuente canonica: `docs/agent_factory/skills/documentation-sync/SKILL.md`. `.claude/` es espejo, no fuente.
