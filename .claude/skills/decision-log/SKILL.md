---
name: decision-log
description: Registra decisiones tecnicas durables en docs/DECISION_LOG.md (arquitectura, seguridad, testing, proveedores, estructura, contrato de agentes, publicacion) con contexto, decision, motivo e impacto.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash
---

# decision-log (wrapper Claude Code)

Usa esta skill cuando una decision sea durable (arquitectura, persistencia, seguridad, testing, proveedores/costos, estructura del repo, onboarding, migraciones, compatibilidad, contrato de agentes o flujo de publicacion). No la uses para cambios triviales.
Agrega una **nueva entrada al inicio** de `docs/DECISION_LOG.md` con el encabezado `## YYYY-MM-DD - Titulo` y los campos: Contexto, Decision, Motivo, Impacto, Alternativas consideradas, Documentos/codigo afectados.
Manten cada campo breve; sin narrativa extensa y sin secretos. Si la decision afecta `AGENTS.md`, `docs/CONTEXT_PACK.md` o `docs/MAINTENANCE_CHECKLIST.md`, actualizalos en el mismo cambio.

> Fuente canonica: `docs/agent_factory/skills/decision-log/SKILL.md`. `.claude/` es espejo, no fuente.
