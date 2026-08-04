---
name: phased-implementation
description: Divide trabajos complejos en fases pequeñas y reversibles, validando entre pasos para mantener el sistema funcional.
allowed-tools: Read, Grep, Glob, Bash
---

# phased-implementation (wrapper Claude Code)

Úsala cuando el cambio toca varios subsistemas o hay drift, no para cambios pequeños y aislados.
1. Define fases pequeñas, reversibles y con un objetivo único cada una.
2. Valida (pruebas o smoke) al final de cada fase antes de pasar a la siguiente.
3. Detente si una fase falla la validación: revierte o corrige y vuelve a validar.
Mantén el sistema funcional entre fases y registra el avance.

> Fuente canonica: `docs/agent_factory/skills/phased-implementation/SKILL.md`. `.claude/` es espejo, no fuente.
