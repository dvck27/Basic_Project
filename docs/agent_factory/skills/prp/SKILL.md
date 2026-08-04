---
name: prp
description: Exige una propuesta tecnica (PRP) antes de un cambio grande y produce un documento completo, basado en el codigo real, que otro agente pueda implementar sin preguntar.
---

# PRP: Propuesta Tecnica Antes de un Cambio Grande

## Purpose
Garantizar que todo cambio de alcance amplio arranque con una propuesta tecnica (PRP) escrita y revisable antes de tocar codigo. El PRP obliga a pensar el problema, el diseño, los archivos afectados, los riesgos y la validacion de forma explicita, de modo que la implementacion sea predecible, auditable y reproducible por cualquier agente. El artefacto se produce a partir de la plantilla `docs/agent_factory/prps/prp-base.md`.

## Use When
Usa esta skill cuando el cambio propuesto encaje en alguno de estos casos:
- Cambia la arquitectura del proyecto o la relacion entre componentes.
- Se agregan subsistemas nuevos o modulos con responsabilidad propia.
- Migraciones de carpetas o reorganizacion de la estructura del repositorio.
- Cambios en el flujo de agentes (orquestacion, roles, contratos entre agentes).
- Cambios de persistencia (formato de datos, esquema, almacenamiento, migracion de datos).
- Cambios de seguridad (manejo de secretos, permisos, superficie de exposicion, autenticacion o autorizacion).
- Cambios en la estrategia o infraestructura de testing.
- Adopcion amplia de un patron externo (una convencion, biblioteca conceptual o enfoque que se replicara en muchos lugares).

Regla practica: si el cambio afecta a mas de un componente, cruza un limite del sistema, o cualquier decision resultante deberia quedar registrada, requiere PRP.

## Do Not Use When
- El cambio es un fix pequeño y acotado (un ajuste local, una correccion puntual, un retoque sin efectos en otros componentes). En ese caso usa el flujo de sprint en lugar de un PRP.
- El cambio ya esta cubierto por un PRP aprobado y solo estas ejecutando lo acordado.
- Es una edicion de documentacion o texto sin impacto en arquitectura, flujo o datos.

## Read First
Antes de redactar el PRP, lee los documentos canonicos para no contradecir decisiones ya tomadas ni el estado actual del proyecto:
- `docs/CONTEXT_PACK.md` — contexto vigente del proyecto: alcance, componentes y estado actual.
- `docs/DECISION_LOG.md` — decisiones previas y su justificacion; evita reabrir lo ya decidido sin motivo.
- `docs/MAINTENANCE_CHECKLIST.md` — verificaciones y responsabilidades de mantenimiento que el cambio debe respetar.
- `AGENTS.md` — reglas y contratos para los agentes que operan en el repositorio.
- `docs/agent_factory/prps/prp-base.md` — plantilla base que estructura el PRP.

## Procedure
1. **Copiar la plantilla.** Duplica `docs/agent_factory/prps/prp-base.md` a un archivo nuevo bajo `docs/agent_factory/prps/` con un nombre descriptivo del cambio. No edites la plantilla base.
2. **Completar todas las secciones** del PRP con contenido real y verificable:
   - **Problem**: que problema o necesidad concreta motiva el cambio.
   - **Objective**: resultado esperado, medible o comprobable.
   - **Current Context**: como funciona hoy la parte afectada, con referencia al estado real del repositorio.
   - **Scope**: que entra en este cambio.
   - **Out of Scope**: que queda explicitamente fuera, para evitar deriva.
   - **Proposed Design**: diseño de la solucion, componentes involucrados y como interactuan.
   - **Affected Files**: rutas concretas que se crearan, modificaran o moveran.
   - **Risks**: riesgos tecnicos, de datos, de seguridad o de compatibilidad, y su mitigacion.
   - **Validation**: como se comprobara que el cambio funciona y no rompe lo existente.
   - **Rollback Plan**: como revertir el cambio si algo falla.
   - **Acceptance Criteria**: condiciones verificables que definen "terminado".
3. **Sin adivinanzas.** Fundamenta cada seccion en el codigo y los documentos reales del repositorio. Si algo se desconoce, marcalo como pregunta abierta o supuesto explicito; no lo presentes como hecho ni inventes detalles.

## Validation
El PRP esta listo cuando otro agente podria implementar el cambio siguiendolo de principio a fin sin necesidad de hacer preguntas. Verifica que:
- Todas las secciones estan completas y coherentes entre si.
- Los archivos afectados estan listados con rutas concretas.
- Los criterios de aceptacion son verificables (no ambiguos).
- El plan de validacion y el de rollback son ejecutables.
- No hay contradicciones con `docs/DECISION_LOG.md` ni con el estado descrito en `docs/CONTEXT_PACK.md`.

## Memory Update
- En `docs/`: si el PRP toma una decision de arquitectura, flujo, persistencia o seguridad, registra esa decision en `docs/DECISION_LOG.md`. Si cambia el alcance o los componentes descritos, actualiza `docs/CONTEXT_PACK.md`. Si introduce nuevas verificaciones o responsabilidades de mantenimiento, refleja eso en `docs/MAINTENANCE_CHECKLIST.md`.
- En el indice operacional: registra el PRP creado (ruta y estado: propuesto / aprobado / implementado) para que quede trazable como trabajo en curso, separado de la documentacion canonica de decisiones.
