# Maintenance Checklist — Basic_Project

> Mantiene alineados **código, specs, tests, README, Context Pack y Decision Log**. Objetivo: cero contradicciones
> entre fuentes y continuidad durable.

## Fuentes de verdad (orden)
Código actual → specs/tests → `docs/CONTEXT_PACK.md` → `README.md` → `docs/DECISION_LOG.md` → memoria operacional → chat.

## Regla de almacenamiento canónico
- Verdad durable del proyecto → `docs/`.
- Capa portable multiagente (skills/prps/runbooks/índice de memoria) → `docs/agent_factory/`.
- Espejo Claude Code → `.claude/` (nunca fuente única).
- Contratos técnicos → `specs/` (cuando existan).
- **Secretos → en ningún archivo versionado.**

## Antes de cambiar código
1. Lee `README.md`, `docs/CONTEXT_PACK.md` y la spec relevante (si existe).
2. Inspecciona el código y localiza los tests afectados.
3. Si el cambio es grande → escribe un **PRP** (`docs/agent_factory/prps/prp-base.md`).

## Cuando cambia el código / comportamiento
Actualiza, según aplique: código → tests → spec → `README` → `CONTEXT_PACK` → `DECISION_LOG`. Declara gaps pendientes.

## Cuándo actualizar el README
Cambian: prerequisitos, dependencias, `.env.example`, comandos de arranque/test/build/lint, URLs/puertos,
entrypoints, flujos principales o límites conocidos.

## Cuándo actualizar el Context Pack
Cambian: propósito, arquitectura, entrypoints, estructura, modelo de memoria, orden de lectura, dependencias
críticas, configuración durable, flujo de publicación/entorno o riesgos duraderos.

## Cuándo registrar en el Decision Log
Decisiones sobre: arquitectura, persistencia, seguridad, testing, proveedores/costos, estructura del repo,
onboarding, migraciones, compatibilidad, contrato de agentes o el flujo de publicación.

## Cuándo tocar la capa de agentes
Cambia el flujo de agentes o el read order → actualiza `AGENTS.md`, los adaptadores y `docs/agent_factory/runbooks/`.
Aprendes de un fallo → skill `postmortem-learning` + Decision Log. `.claude/` desincronizado de la fuente canónica → skill `repo-change-sync`.

## Mínimos SDD / BDD / TDD
- **SDD:** si hay specs, son la fuente técnica; si no, deriva una mini-spec del código y declara vacíos.
- **BDD:** para cambios funcionales, solo los escenarios esenciales (`Given/When/Then`).
- **TDD:** define las pruebas clave (comportamiento, entrada, salida esperada); no generes suites innecesarias.

## Verificación periódica
- ¿README, Context Pack y Decision Log se contradicen? → corregir.
- ¿Docs mencionan comandos/archivos inexistentes? → marcar `Por definir` o eliminar.
- ¿Hay secretos colados en algún archivo versionado? → remediar (revocar + purgar).
- ¿`.claude/skills` divergió de `docs/agent_factory/skills`? → resincronizar.
