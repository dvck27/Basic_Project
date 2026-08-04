---
name: phased-implementation
description: Divide trabajos complejos en fases pequeñas, reversibles y validadas entre pasos; produce un plan por fases que mantiene el sistema funcional en todo momento.
---

# Phased Implementation

## Purpose
Reducir el riesgo de cambios grandes o que tocan varios subsistemas dividiendo el trabajo en fases pequeñas y reversibles, con validación entre cada paso. El objetivo es que el sistema permanezca funcional entre fases y que un fallo quede aislado a una fase concreta, evitando cambios masivos difíciles de revertir o diagnosticar.

## Use When
- El cambio toca varios subsistemas, módulos o límites de responsabilidad a la vez.
- Existe drift entre el estado real y lo documentado, y hay que reconciliar en pasos verificables.
- El trabajo implica migraciones, refactors amplios o reescrituras con riesgo de romper funcionalidad existente.
- Hay incertidumbre sobre el alcance y conviene descubrir problemas temprano, fase por fase.

## Do Not Use When
- El cambio es pequeño, aislado y afecta a un único componente sin dependencias significativas.
- Puede validarse por completo en un solo paso sin dejar el sistema en estado intermedio.
- La sobrecarga de dividir en fases superaría el beneficio (p. ej. un ajuste trivial de una línea).

## Read First
Antes de planificar, revisa los documentos canónicos relevantes del repositorio:
- `docs/CONTEXT_PACK.md` — contexto del proyecto, alcance y límites de los subsistemas afectados.
- `docs/DECISION_LOG.md` — decisiones previas que restringen o justifican el enfoque por fases.
- `docs/MAINTENANCE_CHECKLIST.md` — verificaciones y pasos de mantenimiento que deben respetarse por fase.
- `AGENTS.md` — convenciones operativas, límites de actuación y expectativas para agentes.

## Procedure
1. **Definir fases pequeñas y reversibles.** Descompón el trabajo en fases con un objetivo único y acotado cada una. Cada fase debe poder revertirse con facilidad y no dejar el sistema en un estado roto de forma permanente. Escribe el plan (fase, objetivo, criterio de validación) antes de empezar.
2. **Validar al final de cada fase antes de avanzar.** Al terminar una fase, ejecuta la validación disponible en el proyecto (pruebas, comprobaciones de humo o verificación funcional acordada) y confirma que pasa antes de iniciar la siguiente. No encadenes fases sin verificar la anterior.
3. **Mantener un objetivo claro por fase.** Cada fase persigue una sola meta observable. Si aparece trabajo adicional, anótalo como fase futura en lugar de ampliar la fase en curso.
4. **Detenerse si una fase falla la validación.** Si una fase no supera su validación, detente. Revierte esa fase o corrígela y vuelve a validar antes de continuar; nunca avances sobre una fase no verificada.

## Validation
- Cada fase queda verificada mediante la comprobación acordada (pruebas, smoke o verificación funcional) y el resultado se registra.
- El sistema permanece funcional entre fases: no hay estados intermedios rotos que persistan al pasar a la siguiente fase.
- Ante un fallo, existe un punto de retorno claro (la fase anterior verificada) al que revertir.

## Memory Update
- En `docs/`: registra en `docs/DECISION_LOG.md` la decisión de abordar el trabajo por fases y su motivo; actualiza `docs/CONTEXT_PACK.md` si el alcance o los límites de los subsistemas cambian; refleja en `docs/MAINTENANCE_CHECKLIST.md` cualquier verificación nueva y recurrente que surja del trabajo.
- En el índice operacional: anota el estado de avance por fases (fase actual, fases completadas y validadas, fase detenida por fallo). Este seguimiento operativo no reemplaza a los docs canónicos: lo duradero va a `docs/`, el estado de ejecución al índice operacional.

## Common Errors
- Definir fases demasiado grandes que vuelven a introducir el riesgo de cambio masivo que se pretendía evitar.
- Avanzar a la siguiente fase sin validar la anterior o sin registrar el resultado.
- Mezclar varios objetivos en una misma fase, lo que dificulta aislar el origen de un fallo.
- No dejar un punto de retorno reversible, impidiendo revertir limpiamente una fase fallida.
