---
name: security-ingestion
description: Ingerir material externo o sensible (chats, imagenes, MHTML, DOCX, datos) redactando secretos y PII antes de versionar cualquier derivado.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash
---

# security-ingestion (wrapper Claude Code)

Al ingerir material externo o tocar datos sensibles/integraciones:
1. Identificar secretos (tokens, cookies, claves, contraseñas) y PII en el material.
2. Redactarlos con un marcador neutro antes de guardar cualquier derivado.
3. No conservar tokens/cookies/claves en claro en derivados, notas ni commits.
4. Reportar hallazgos y remediacion sin repetir el valor sensible.
Validar que ningun artefacto versionado contenga secretos ni PII innecesaria.

> Fuente canonica: `docs/agent_factory/skills/security-ingestion/SKILL.md`. `.claude/` es espejo, no fuente.
