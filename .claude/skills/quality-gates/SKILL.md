---
name: quality-gates
description: Define el conjunto minimo de pruebas y checks que realmente prueban un cambio, sin agregar tooling innecesario.
allowed-tools: Read, Grep, Glob, Bash
---

# quality-gates (wrapper Claude Code)

Aplica ante cambios de comportamiento o nuevas integraciones; omite si no hubo cambio observable.
1. Identifica los tests mas pequeños relevantes que ejerciten el cambio.
2. Si faltan tests, agrega un smoke check minimo que valide el camino principal.
3. Prefiere el tooling existente; no inventes comandos ni dependencias nuevas.
4. Documenta la validacion que no pudo automatizarse. Si el repo aun no tiene stack/tests, define el gate como pendiente y agnostico.

> Fuente canonica: `docs/agent_factory/skills/quality-gates/SKILL.md`. `.claude/` es espejo, no fuente.
