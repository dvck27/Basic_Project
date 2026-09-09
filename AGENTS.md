# AGENTS.md — Contrato operativo para agentes de IA

> **Punto de entrada ÚNICO** para cualquier agente. `CLAUDE.md`, `GEMINI.md` y `CODEX.md` son adaptadores;
> no son contratos alternativos.

## Misión
Mantener **PAI Auto** como una aplicación local-first pequeña, predecible y fácil de ejecutar. La prioridad es
resolver el flujo Registro Diario SIS → validación → ejecución → verificación → auditoría sin reconstruir la
complejidad del repositorio de investigación `vacunacion-paiweb`.

## Jerarquía de fuentes de verdad
1. Código fuente actual.
2. Specs / contratos técnicos / tests.
3. `docs/CONTEXT_PACK.md`.
4. `README.md`.
5. `docs/DECISION_LOG.md`.
6. Memoria operacional de agentes.
7. Repositorios de referencia.
8. Historial de chat.

El repositorio `dvck27/vacunacion-paiweb` es **fuente de conocimiento y evidencia**, no una dependencia de runtime
ni una autorización para copiar su arquitectura completa.

## Orden de lectura
1. `README.md`
2. `docs/CONTEXT_PACK.md`
3. `specs/WORKFLOW.md`
4. `docs/DECISION_LOG.md`
5. `docs/MAINTENANCE_CHECKLIST.md`
6. código y tests afectados

## Reglas de producto
- **Un administrador.** No introducir roles, comités, firmas múltiples ni gates distribuidos salvo nueva decisión explícita.
- **Un proceso local.** Evitar Redis, Celery, Docker, SQL Server o microservicios si el problema cabe en el proceso actual.
- **Lote = filas fuente.** 1/20/50/100 se cuenta por `source_row`; todas las aplicaciones de una fila viajan juntas.
- **Determinismo clínico.** No usar LLM ni fuzzy matching para identidad, biológico, dosis, lote o campos clínicos.
- **No inventar datos.** En modo real, todo campo requerido sin fuente debe venir explícitamente del administrador o fallar.
- **Idempotencia antes de velocidad.** Nunca marcar una aplicación procesada antes de verificar el resultado del gateway.
- **Continuar por aplicación.** Un fallo individual no debe detener el resto del lote; un fallo de sesión/gateway sí puede abortar.
- **Real empieza pequeño.** `PAI_AUTO_REAL_MAX_ROWS` default 1 hasta validar escritura real; escalar no requiere cambiar código.
- **Nada de pacientes reales en Git.** `runtime/`, XLSX, DB, tokens, credenciales y artefactos de navegador son locales.

## Reglas de ingeniería
- Inspecciona antes de editar.
- Cambios mínimos, reversibles y cubiertos por tests cuando cambia comportamiento.
- No inventes selectores PAIWEB: documenta procedencia y falla cerrado ante divergencia.
- Mantén `README`, `CONTEXT_PACK`, `WORKFLOW`, `DECISION_LOG` y tests sincronizados.
- Cambios grandes → PRP en `docs/agent_factory/prps/`.
- No hagas operaciones Git destructivas ni reescribas historial sin autorización explícita.

## Secretos
Nunca guardar tokens, contraseñas, cookies, llaves, archivos OAuth ni datos de pacientes en archivos versionados.
La UI puede recibir credenciales en memoria; el código no debe persistir la contraseña PAIWEB.

## Uso de skills
Las skills canónicas siguen en `docs/agent_factory/skills/`. Úsalas como metodología; no deben imponer arquitectura
adicional al producto.

## Cierre de cambios
Antes de publicar:
1. `python -m pytest`
2. `ruff check .` cuando Ruff esté instalado
3. smoke de la UI si cambió la web
4. revisar que no entren `runtime/`, XLSX, DB o secretos
5. actualizar documentación durable si cambió comportamiento
6. publicar por rama + PR para cambios funcionales; no saltar directamente a `main` durante pruebas reales
