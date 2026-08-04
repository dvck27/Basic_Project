# PRP — Plantilla base (Product/Problem Requirement Prompt)

> Usa esta plantilla cuando un cambio sea demasiado grande para una nota corta: arquitectura, subsistemas,
> migraciones, persistencia, seguridad, testing o adopción amplia de patrones externos.

```markdown
# PRP: <título>

## Problem
Qué está roto o falta, y por qué importa (impacto en usuario o mantenibilidad).

## Objective
Resultado buscado, en una frase.

## Current Context
Arquitectura/flujo actual relevante; código o spec que aplica.

## Scope
Qué entra en el cambio.

## Out of Scope
Qué explícitamente NO se toca.

## Proposed Design
Cómo se implementa (pseudocódigo, módulos nuevos, cambios de archivo).

## Affected Files
- `ruta/archivo` → qué cambia
- `docs/CONTEXT_PACK.md` → si cambia contexto durable
- `tests/...` → nueva cobertura

## Risks
Seguridad, persistencia, compatibilidad, portabilidad.

## Validation
Prueba unitaria / smoke check / regresión / validación manual (si no es automatizable).

## Rollback Plan
Cómo deshacer si falla.

## Acceptance Criteria
- [ ] Cambios implementados
- [ ] Tests en verde
- [ ] Docs sincronizados (README, Context Pack, Decision Log si aplica)
- [ ] Sin regresiones
```
