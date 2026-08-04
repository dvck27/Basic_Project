# AGENTS.md — Contrato operativo para agentes de IA

> **Punto de entrada ÚNICO** para cualquier agente (Claude, Gemini, Codex, Antigravity u otro).
> Léelo completo antes de tocar nada. `CLAUDE.md`, `GEMINI.md` y `CODEX.md` solo redirigen aquí y añaden
> matices del proveedor; **no** son contratos alternativos.

## Misión
Operar este repositorio con **continuidad de contexto durable**: cualquier agente nuevo debe poder entender el
proyecto, retomar el trabajo y aplicar reglas de ingeniería consistentes **sin depender del historial del chat**.
Este repositorio es una **base agent-ready agnóstica**: la metodología no asume ningún stack (aún no hay uno definido).

## Jerarquía de fuentes de verdad (ante contradicciones)
1. Código fuente actual.
2. Specs / contratos técnicos / tests.
3. Context Pack durable — `docs/CONTEXT_PACK.md`.
4. `README.md`.
5. Decision Log — `docs/DECISION_LOG.md`.
6. Memoria operacional de agentes — `docs/agent_factory/memory/`, `.claude/memory/`.
7. Repositorio guía / referencias externas.
8. Historial de chat (descartable).

El repositorio guía es **referencia, no autoridad** superior al proyecto.

## Ubicaciones canónicas
- `docs/` → **verdad durable** del proyecto (versionada).
- `docs/agent_factory/` → **capa portable multiagente** (skills, prps, runbooks, índice de memoria).
- `.claude/` → **espejo/adaptador** para Claude Code (NO es fuente).
- `specs/` y código → contratos técnicos y comportamiento real (cuando existan).

## Orden de lectura (antes de cambiar algo)
1. `README.md`
2. `docs/CONTEXT_PACK.md`
3. `docs/DECISION_LOG.md`
4. `docs/MAINTENANCE_CHECKLIST.md`
5. `specs/` y el código afectado (cuando existan)

## Reglas de trabajo
- **Inspecciona antes de editar.** Primero entiende, luego cambia.
- **Cambios mínimos y reversibles.** No rompas lo que ya funciona.
- **Solo lo verificable.** No inventes comandos, rutas, dependencias, badges ni arquitectura: marca `No verificado` o `Por definir`.
- **Sin secretos.** Nunca guardes tokens, contraseñas, cookies, llaves API ni perfiles personales en ningún archivo. Redacta material externo.
- **Worktree sucio:** no borres, reviertas ni mezcles cambios ajenos; haz *staging* selectivo; ante conflicto directo, **detente y pregunta**.
- **Nada destructivo sin autorización explícita:** `git reset --hard`, `git checkout --`, borrados masivos o reescritura de historial.
- **SDD/BDD/TDD:** si cambia el comportamiento, actualiza spec + tests; mantén los docs vivos sincronizados.
- **PRP para cambios grandes** (arquitectura, subsistemas, migraciones, seguridad, persistencia); **sprint** para fixes pequeños; registra decisiones durables en el Decision Log.

## Uso de skills
Las **skills canónicas** viven en `docs/agent_factory/skills/` (agnósticas, multiagente). `.claude/skills/` son
*wrappers* de compatibilidad para Claude Code. Empieza normalmente con **`repo-primer`** (o **`rescue-context`**
si perdiste el hilo). Inventario: `docs/agent_factory/skills/SKILLS_README.md`.

## Expectativas del agente
- Prefiere los docs del repo sobre el historial de chat.
- Al terminar un cambio, deja `README`, `CONTEXT_PACK`, `DECISION_LOG` y tests **coherentes** con lo hecho (ver `docs/MAINTENANCE_CHECKLIST.md`).
- Convierte fallos recurrentes en reglas (skill `postmortem-learning`).
- Publica con el flujo del repo: comando `/subir` o `git add` + `git commit` + `git push origin main`. Detalles en `docs/CONTEXT_PACK.md` → *Publicación y entorno*.
