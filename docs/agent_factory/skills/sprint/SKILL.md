---
name: sprint
description: Ejecuta un fix pequeño, acotado y de bajo riesgo con ceremonia mínima; produce un cambio localizado validado sin efectos colaterales.
---

# Sprint

## Purpose
Resolver un problema puntual mediante el cambio más pequeño posible, con la menor ceremonia. Está pensada para fixes localizados que no alteran la arquitectura ni requieren un PRP (Product Requirement Prompt). El objetivo es corregir el comportamiento observado sin abrir un flujo de planificación completo.

## Use When
- El fix es localizado: afecta un archivo o un conjunto muy reducido y contiguo.
- El cambio no modifica la arquitectura ni contratos públicos entre módulos.
- No requiere un PRP ni un plan por fases para entenderse o ejecutarse.
- El problema y su solución son claros; el riesgo de regresión es bajo.
- Se puede validar con una comprobación pequeña y directa.

## Do Not Use When
- El cambio es grande, transversal o cruza varios módulos.
- Toca la arquitectura, contratos de interfaz o decisiones de diseño.
- Introduce ambigüedad de alcance o requiere descubrir requisitos.
- Necesita coordinación entre partes o pasos secuenciales dependientes.
- En esos casos usa las skills `prp` y `phased-implementation`.

## Read First
Antes de tocar código, revisa los documentos canónicos relevantes al área:
- `docs/CONTEXT_PACK.md` — contexto operativo, convenciones y límites del repositorio.
- `docs/DECISION_LOG.md` — decisiones vigentes que podrían restringir el fix.
- `docs/MAINTENANCE_CHECKLIST.md` — verificaciones esperadas antes de cerrar un cambio.
- `AGENTS.md` — reglas de trabajo para agentes en este repositorio.

Si el fix roza un área con decisión previa registrada, respétala o documenta la desviación en `docs/DECISION_LOG.md`.

## Procedure
1. **Confirmar el alcance mínimo.** Reproduce o localiza el problema. Delimita el cambio a lo estrictamente necesario. Si al confirmar el alcance descubres que el cambio crece o cruza módulos, detente y escala a `prp` + `phased-implementation`.
2. **Hacer el cambio mínimo.** Aplica únicamente la modificación que corrige el comportamiento. No refactorices de paso, no cambies estilo ni toques código no relacionado.
3. **Validar con el check más pequeño.** Ejecuta la comprobación más acotada que demuestre el comportamiento corregido (la prueba, verificación o inspección que ya exista en el repositorio para esa área). No inventes comandos ni herramientas: usa lo que el repositorio ya define. Consulta `docs/MAINTENANCE_CHECKLIST.md` para saber qué verificación aplica.
4. **Actualizar docs solo si cambió el onboarding o el uso.** Si el fix modifica cómo se instala, configura o usa algo, actualiza la documentación correspondiente. Si el comportamiento visible no cambió, no toques los docs.

## Validation
- El fix resuelve el problema reportado de forma verificable.
- No hay efectos colaterales: nada ajeno al problema cambia de comportamiento.
- La comprobación acotada pasa y refleja el comportamiento esperado.
- El diff es pequeño y su intención es evidente al leerlo.

## Memory Update
- En `docs/`: actualiza solo lo que cambió de cara al usuario o al onboarding.
  - Si cambió el uso, instalación o configuración: refleja el ajuste en `docs/CONTEXT_PACK.md`.
  - Si el fix desvió o consolidó una decisión: registra una entrada breve en `docs/DECISION_LOG.md`.
- En el índice operacional (no canónico): registra el fix como una entrada breve de bitácora (qué se corrigió y por qué), sin duplicar el contenido de los docs canónicos.
- Si el comportamiento visible y el onboarding no cambiaron, no actualices `docs/`; basta la nota operacional.

## Common Errors
- Ampliar el alcance "ya que estamos": rompe la premisa de la skill; escala a `prp`.
- Refactorizar o reformatear junto al fix: contamina el diff y esconde la corrección.
- Validar de más: usa el check mínimo que prueba el comportamiento, no la suite completa.
- Actualizar docs sin necesidad: solo si el onboarding o el uso cambió.
