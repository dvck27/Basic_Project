# SaaS Factory Adoption Report — Basic_Project

> Qué se tomó del repo guía y cómo se adaptó. Sirve para repetir el proceso en otros repositorios.

## Fuente analizada
Repo guía Orion: `...\Orion\Python_Utilities_Tools-main\Python_Utilities_Tools-main` (monorepo Python/Streamlit
con metodología multiagente madura). Inputs adicionales del usuario en `docs/`: `PROMPT_README_REPOSITORIOS.docx`,
`PROMPT_MEMORIA_PERSISTENTE_REPOSITORIOS.docx` (estándares propios de README y memoria persistente).

## Objetivo de la adopción
Instalar una capa **agnóstica** de operación por agentes (continuidad, memoria persistente, docs vivos, PRPs,
skills, quality gates) sobre un repo vacío, **sin imponer el stack del guía** ni convertirlo en un SaaS.

## Elementos adoptados (casi iguales, agnósticos)
- Contrato neutral `AGENTS.md` como **punto de entrada único** + adaptadores por proveedor (`CLAUDE/GEMINI/CODEX`).
- Jerarquía de fuentes de verdad y **orden de lectura**.
- Capa portable `docs/agent_factory/` (skills, prps, runbooks, índice de memoria) como **fuente canónica**; `.claude/` como espejo.
- **16 skills** canónicas (repo-primer, memory-manager, readme-maintainer, context-pack-maintainer, decision-log,
  documentation-sync, prp, phased-implementation, sprint, codebase-analyst, quality-gates, security-ingestion,
  repo-change-sync, rescue-context, skill-creator, postmortem-learning).
- Docs durables: Context Pack, Decision Log, Maintenance Checklist. Disciplina de memoria (runtime vs proyecto vs contratos).
- Plantilla PRP y disciplina de postmortem → control de ingeniería.

## Elementos adaptados
- **Estructura:** se usa `docs/agent_factory/` (patrón real del guía) en vez de `.agents/` (idealizado del prompt, vacío en el guía).
- **Nombres:** sin prefijos propios (`ORION_` → nombres genéricos: `CONTEXT_PACK.md`, `DECISION_LOG.md`).
- **Idioma/contenido:** neutro y agnóstico; se alinearon `readme-maintainer` y la memoria con los estándares del usuario (`docs/*.docx`).
- **Wrappers Claude:** las 16 skills tienen espejo fino en `.claude/skills/` con `allowed-tools`.

## Elementos RECHAZADOS (no aplican a este repo)
Next.js, React, Tailwind, Supabase, Vercel, Stripe, Resend, npm/pnpm, estructura `src/app`, billing/landing/mobile,
Streamlit, `orion/` framework, ffmpeg/yt-dlp/opencv y demás dependencias del dominio Orion, Pyrefly y cualquier
herramienta específica de lenguaje. Motivo: el repo destino es agnóstico y no usa ese stack.

## Mapeo al repositorio destino
| Guía (Orion) | Destino (Basic_Project) |
|---|---|
| `AGENTS.md` + `CLAUDE/GEMINI/CODEX.md` | Igual, agnóstico |
| `docs/ORION_CONTEXT_PACK.md` | `docs/CONTEXT_PACK.md` |
| `docs/ORION_DECISION_LOG.md` | `docs/DECISION_LOG.md` |
| `docs/ORION_MAINTENANCE_CHECKLIST.md` | `docs/MAINTENANCE_CHECKLIST.md` |
| `docs/agent_factory/**` | Igual (16 skills, prps, runbooks, memory) |
| `.claude/**` | Espejo (wrappers, memory, PRPs, settings) + `commands/subir.md` existente |

## Skills creadas
Las 16 canónicas + 16 wrappers Claude (ver `docs/agent_factory/skills/SKILLS_README.md`).

## Riesgos detectados
- Repo sin código: skills dependientes de código son guía metodológica hasta que exista stack.
- Volumen de archivos: mitigado con propósito claro por artefacto y este reporte + checklist de mantenimiento.
- Binarios `.docx` en `docs/` (movidos desde `doc/`): son referencia; evaluar si mantenerlos versionados.

## Decisiones tomadas
Registradas en `docs/DECISION_LOG.md` (entrada 2026-07-01 "Adoptar capa agent-ready agnóstica").

## Validaciones ejecutadas
Ver el commit de adopción: estructura creada, `AGENTS.md` como entrada, skills canónicas + wrappers, grep de
secretos = 0, coherencia README/Context Pack, sin stack impuesto.

## Recomendaciones para otros repositorios
1. Copiar `AGENTS.md`, `docs/agent_factory/`, `docs/CONTEXT_PACK.md|DECISION_LOG.md|MAINTENANCE_CHECKLIST.md` y adaptar nombres/rutas.
2. Rellenar el Context Pack con el stack real y declarar gaps.
3. Mantener `docs/` como fuente; `.claude/` solo como espejo; nunca guardar secretos.
