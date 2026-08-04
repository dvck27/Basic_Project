---
name: repo-primer
description: Reconstruye el modelo mental del repo desde fuentes repo-local al iniciar o retomar una sesion y produce un resumen operativo compacto.
allowed-tools: Read, Grep, Glob, Bash
---

# repo-primer (wrapper Claude Code)

Usala en chat nuevo, al retomar trabajo o antes de un cambio mediano o grande; no en fixes triviales de una linea.
1. Enuncia el objetivo actual en una frase.
2. Lee en orden `AGENTS.md`, `docs/CONTEXT_PACK.md`, `docs/DECISION_LOG.md`, `docs/MAINTENANCE_CHECKLIST.md`.
3. Inspecciona el area de la tarea (`git status` y archivos relevantes); no asumas stack ni comandos.
4. Devuelve: objetivo del proyecto, estado actual, docs durables, archivos afectados y proximo paso seguro.
Meta: que otro agente pueda continuar sin el historial del chat.

> Fuente canonica: `docs/agent_factory/skills/repo-primer/SKILL.md`. `.claude/` es espejo, no fuente.
