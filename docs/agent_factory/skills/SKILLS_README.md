# Skills — inventario (capa canónica agnóstica)

16 skills reutilizables por cualquier agente. Fuente canónica aquí; `.claude/skills/` son wrappers de compatibilidad.

## Formato de cada skill (`<nombre>/SKILL.md`)
Frontmatter (`name`, `description`) + secciones: **Purpose · Use When · Do Not Use When · Read First ·
Procedure · Validation · Memory Update** (más *Common Errors* cuando aporta).

## Catálogo
| Skill | Para qué |
|---|---|
| `repo-primer` | Recuperar contexto al iniciar una sesión. |
| `memory-manager` | Mantener índice operacional sin duplicar los docs canónicos. |
| `readme-maintainer` | Alinear el README con el comportamiento real (solo lo verificable). |
| `context-pack-maintainer` | Mantener el Context Pack durable y exacto. |
| `decision-log` | Registrar decisiones técnicas durables. |
| `documentation-sync` | Evitar divergencia entre código y docs cuando cambia el comportamiento. |
| `prp` | Exigir propuesta técnica antes de un cambio grande. |
| `phased-implementation` | Dividir trabajos complejos en fases con validación entre pasos. |
| `sprint` | Fix pequeño y acotado con ceremonia mínima. |
| `codebase-analyst` | Mapear arquitectura, dependencias e impacto (sin modificar código). |
| `quality-gates` | Definir el conjunto mínimo de pruebas/checks que prueban el cambio. |
| `security-ingestion` | Procesar material externo/sensible con redacción de secretos. |
| `repo-change-sync` | Sincronizar el espejo `.claude/` con la fuente canónica. |
| `rescue-context` | Reconstruir el estado cuando se pierde el chat o hay drift. |
| `skill-creator` | Crear/refinar skills con el formato robusto (evitar skills triviales). |
| `postmortem-learning` | Convertir fallos en reglas, tests de regresión y documentación durable. |

## Mapeo con los estándares del usuario (`docs/*.docx`)
`context-pack-maintainer`≈`repo-context-pack`, `rescue-context`≈`memory-continuity`, `codebase-analyst`≈`architecture-map`,
`readme-maintainer`≈`onboarding-runbook`, `maintenance-checklist`→`docs/MAINTENANCE_CHECKLIST.md`.
