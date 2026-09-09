# Decision Log — Basic_Project

> Decisiones técnicas **durables**. No registrar cambios triviales. Formato por entrada (más reciente arriba):
> Contexto · Decisión · Motivo · Impacto · Alternativas · Documentos/código afectados.

## 2026-09-08 — Adoptar PAI Auto como aplicación y mantener el flujo compacto
- **Contexto:** `Basic_Project` era solo bootstrap. Se necesita una versión nueva del sistema de vacunación, funcional para pruebas, sin heredar la complejidad institucional de `vacunacion-paiweb`.
- **Decisión:** Python/FastAPI/Jinja2 + SQLite + openpyxl; Playwright/Gmail OAuth como extras reales. Un solo administrador. Lotes de 1/20/50/100 **filas**. Simulador y gateway real comparten la misma interfaz.
- **Motivo:** máxima portabilidad y un único proceso local, preservando solo idempotencia, verificación posterior y contrato del dato.
- **Impacto:** el repositorio deja de ser agnóstico y pasa a tener una aplicación Python. `runtime/` es local; no se introducen Docker, Redis, SQL Server ni servicios obligatorios.
- **Alternativas:** recortar el Django original, usar n8n como runtime o introducir un LLM en el camino crítico — descartadas para V0.
- **Afectados:** `src/pai_auto/**`, `tests/**`, `specs/WORKFLOW.md`, `README.md`, `docs/CONTEXT_PACK.md`.

## 2026-09-08 — Escritura real requiere una aprobación de corrida, no gates distribuidos
- **Contexto:** el original no había ejecutado escrituras reales y tenía múltiples gates/roles. El nuevo sistema debe tener un solo administrador sin perder el control sobre una mutación clínica.
- **Decisión:** una confirmación explícita en UI al inicio; valores operativos obligatorios sin defaults implícitos; `PAI_AUTO_REAL_MAX_ROWS=1` hasta validar una fila y luego configurable hasta 100 sin cambiar código.
- **Motivo:** quitar el cuello de botella humano del procesamiento normal sin convertir una prueba no validada en una escritura masiva accidental.
- **Impacto:** simulador usa 1/20/50/100 desde el primer día; real puede escalar por configuración local después de la primera validación.
- **Afectados:** `src/pai_auto/app.py`, `templates/index.html`, `README.md`, `specs/WORKFLOW.md`.

## 2026-09-08 — El LLM no decide datos clínicos
- **Contexto:** se considera un LLM local como nodo tipo n8n.
- **Decisión:** dejarlo fuera de V0 y del camino determinístico. Futuro uso: diagnóstico/explicación/asistencia.
- **Motivo:** identidad, dosis, lote y campos clínicos deben ser reproducibles y auditables.
- **Impacto:** el motor funciona en equipos estándar sin descargar modelos y no depende de inferencia probabilística.
- **Afectados:** arquitectura y `specs/WORKFLOW.md`.

## 2026-08-04 — Migrar la publicación canónica de Gitea a GitHub
- **Contexto:** la carpeta agent-ready se publicará como repositorio `dvck27/Basic_Project`; el remoto de GitHub existe y está vacío, y esta copia local todavía no tenía metadatos Git.
- **Decisión:** usar `https://github.com/dvck27/Basic_Project.git` como único remoto `origin`, rama `main`; publicar con push explícito y configurar localmente la identidad `Dave <dvck27@users.noreply.github.com>`.
- **Motivo:** establecer GitHub como fuente remota canónica, evitar depender de hooks no versionados y no exponer el correo personal en commits.
- **Impacto:** se sustituyen las referencias operativas a Gitea en contratos, onboarding, Context Pack, runbook y `/subir`; las tres decisiones de publicación de 2026-07-01 quedan supersedidas y se conservan solo como historial.
- **Alternativas:** mantener Gitea como principal y GitHub como espejo, o publicar un snapshot sin sincronizar la documentación — descartadas.
- **Afectados:** `README.md`, `AGENTS.md`, `CLAUDE.md`, `.claude/commands/subir.md`, `docs/CONTEXT_PACK.md`, runbook y configuración Git local.

## 2026-07-01 — Adoptar capa agent-ready agnóstica (metodología SaaS Factory / Orion)
- **Contexto:** repo casi vacío; se decide dotarlo desde el inicio de una metodología madura de agentes, memoria persistente y documentación viva, tomando como guía el repo Orion.
- **Decisión:** crear `AGENTS.md` (entrada única) + adaptadores `CLAUDE/GEMINI/CODEX`; capa portable en `docs/agent_factory/` (16 skills + prps + runbook + índice de memoria); docs durables en `docs/`; espejo en `.claude/`. Todo **agnóstico** (sin stack impuesto).
- **Motivo:** continuidad de contexto entre agentes/sesiones sin depender del chat; reglas de ingeniería consistentes; base reutilizable.
- **Impacto:** ~50 archivos markdown nuevos; ninguna lógica existente se toca; `.claude/skills` queda como espejo, no fuente.
- **Alternativas:** usar `.agents/` (idealizado del prompt, vacío en el guía) → descartado a favor de `docs/agent_factory/` (patrón real y probado). Copiar el guía literal → descartado (impondría Python/Streamlit).
- **Afectados:** `AGENTS.md`, `docs/**`, `.claude/**`, `README.md`, `docs/SAAS_FACTORY_ADOPTION_REPORT.md`.

## 2026-07-01 — Auto-push por hook post-commit + interfaz por lenguaje natural (supersedida 2026-08-04)
- **Contexto:** se pidió poder subir a Gitea "automáticamente" y por lenguaje natural a través del agente IA.
- **Decisión:** hook `.git/hooks/post-commit` que hace `git push`; alias `git subir`; comando Claude `/subir`; `CLAUDE.md`/Context Pack documentan el flujo.
- **Motivo:** publicación sin fricción; cualquier commit se sube solo.
- **Impacto:** todo commit local se publica al instante (repo privado → aceptable). El hook no se versiona (vive en `.git/hooks`).
- **Alternativas:** push manual (más fricción); GitHub Actions/CI (innecesario para este repo local).
- **Afectados:** `.git/hooks/post-commit`, `.claude/commands/subir.md`, alias global git.

## 2026-07-01 — Autenticación por PAT + Git Credential Manager para Gitea (supersedida 2026-08-04)
- **Contexto:** el repo Gitea es privado por HTTP; se necesitaba push sin fricción y seguro.
- **Decisión:** usar un **PAT** de Gitea (no la contraseña), almacenado por GCM (`provider generic` para el host). Blindaje de secretos en `.gitignore` (`Token_*.txt`, `*.pat`, `.env`, `*.key`).
- **Motivo:** credencial revocable, compatible con 2FA, sin exponer la contraseña; evitar recomits de secretos.
- **Impacto:** primer push interactivo (una vez), luego automático. Un PAT llegó a filtrarse en un commit y se **purgó del historial** (force-push) y se rotó.
- **Alternativas:** usuario+contraseña (menos seguro, falla con 2FA); SSH (más robusto, requiere puerto SSH) — pendiente.
- **Afectados:** `.gitignore`, config global de git (credential/proxy).

## 2026-07-01 — Bypass de proxy corporativo para el Gitea interno (supersedida 2026-08-04)
- **Contexto:** git recibía HTTP 503 al empujar; causa = proxy corporativo que no enruta al host interno (`10.10.74.133`, LAN).
- **Decisión:** `git config --global "http.http://python.virreysolisips.com.co:53000/.proxy" ""` (proxy vacío solo para ese host).
- **Motivo:** conectar directo al Gitea interno sin afectar el resto del tráfico (que sigue por el proxy).
- **Impacto:** push/fetch/ls-remote funcionan; el resto de la red no cambia.
- **Alternativas:** `NO_PROXY` a nivel usuario (más amplio/invasivo) — no necesario.
- **Afectados:** config global de git; documentado en `docs/CONTEXT_PACK.md`.
