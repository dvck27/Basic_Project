---
name: readme-maintainer
description: Alinea el README con el comportamiento real y verificable del repositorio cuando cambian instalacion, arranque, pruebas, build, lint, entrypoints, URLs/puertos, flujos o dependencias.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash
---

# readme-maintainer (wrapper Claude Code)

Usala cuando haya evidencia en codigo/config de que cambio instalacion, arranque, pruebas, build, lint, entrypoints, URLs/puertos, flujos o dependencias.
Verifica primero el comportamiento real leyendo codigo y configuracion; documenta solo lo comprobable y marca lo demas como `No verificado` o `Por definir`.
Actualiza solo las secciones afectadas del README; no afirmes CI/CD, licencia, despliegue ni herramientas inexistentes; sin secretos.
Este repo es agnostico: no asumas ningun lenguaje, framework ni runtime.
Valida que un mantenedor nuevo pueda instalar, ejecutar y probar el proyecto siguiendo solo el README.

> Fuente canonica: `docs/agent_factory/skills/readme-maintainer/SKILL.md`. `.claude/` es espejo, no fuente.
