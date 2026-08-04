---
name: codebase-analyst
description: Analiza arquitectura, dependencias, patrones y puntos criticos SIN modificar codigo; usala antes de un cambio mediano+, nueva feature o refactor para planear con confianza y localizar los tests afectados.
---

# Codebase Analyst

## Purpose
Comprender la estructura real del codigo antes de intervenirlo. Produce un mapa de arquitectura, dependencias, patrones vigentes y puntos criticos, junto con el linaje y el impacto esperado del cambio propuesto. Es una skill de solo lectura: no edita, no reformatea, no ejecuta migraciones ni escribe archivos de codigo. Su salida es un analisis accionable que reduce el riesgo de la implementacion posterior.

## Use When
- Antes de un cambio de tamano mediano o mayor.
- Al iniciar una nueva feature que toca modulos que no dominas.
- Antes de un refactor que altera limites de modulos, contratos o flujos de datos.
- Cuando necesitas entender el impacto de un cambio en areas que no conoces.
- Cuando debes localizar los tests que cubren (o deberian cubrir) el area afectada.

## Do Not Use When
- Ya conoces el area y el cambio es trivial (correccion de texto, ajuste de una constante, typo).
- El cambio esta aislado y su alcance es evidente sin analisis previo.
- Solo necesitas ejecutar la implementacion de un plan ya validado; en ese caso pasa directo a la skill de cambio correspondiente.

## Read First
Antes de analizar, revisa los documentos canonicos del repositorio para no repetir trabajo ni contradecir decisiones ya tomadas:
- `docs/CONTEXT_PACK.md` — contexto general, arquitectura declarada, convenciones y limites del sistema.
- `docs/DECISION_LOG.md` — decisiones tecnicas previas y su justificacion; evita reabrir debates cerrados.
- `docs/MAINTENANCE_CHECKLIST.md` — puntos de mantenimiento, deuda tecnica conocida y zonas fragiles.
- `AGENTS.md` — reglas operativas para agentes, alcance permitido y flujo de trabajo esperado.

## Procedure
1. **Mapear entrypoints, modulos y dependencias.** Identifica los puntos de entrada del sistema (arranque, comandos, handlers, tareas). Lista los modulos principales y como se relacionan entre si. Distingue dependencias internas de externas y anota su direccion (quien depende de quien).
2. **Trazar el flujo relevante a la tarea.** Sigue el recorrido concreto que atraviesa el cambio: desde el entrypoint pertinente hasta el limite donde termina el efecto. Marca los contratos (interfaces, formatos de datos, eventos) que cruza y donde se transforman los datos.
3. **Identificar tests existentes y riesgos estructurales.** Localiza los tests que cubren el area (unitarios, integracion, extremo a extremo) y detecta las zonas sin cobertura. Anota riesgos estructurales: acoplamientos fuertes, dependencias ciclicas, estado compartido, efectos secundarios ocultos y puntos frontera con sistemas externos.
4. **Reportar linaje e impacto.** Entrega un resumen con: el mapa relevante, el flujo trazado, los tests afectados, los riesgos detectados y el linaje del cambio (que se toca, que se propaga aguas abajo y que queda fuera de alcance).

## Validation
El analisis se considera valido cuando permite:
- Planear el cambio con confianza, sabiendo que modulos y contratos se veran afectados.
- Localizar con precision los tests existentes que cubren el area y los que faltan.
- Anticipar los riesgos estructurales antes de escribir codigo.
Nota: esta skill no edita archivos. Si en algun momento necesitas modificar codigo, esta fuera del alcance de esta skill; deten el analisis y cambia a la skill de implementacion correspondiente.

## Memory Update
- **En `docs/` (memoria duradera):** si el analisis revela hechos arquitectonicos estables, decisiones implicitas o deuda tecnica relevante, refleja lo pertinente en `docs/CONTEXT_PACK.md`, registra decisiones nuevas en `docs/DECISION_LOG.md` y anota zonas fragiles o de mantenimiento en `docs/MAINTENANCE_CHECKLIST.md`.
- **En el indice operacional (memoria de trabajo):** deja constancia del hallazgo puntual, el flujo trazado y los tests afectados como notas de la tarea en curso, sin promoverlas a documentacion canonica salvo que sean estables y reutilizables.
- Regla practica: lo que sigue siendo cierto entre tareas va a `docs/`; lo que solo importa para esta tarea va al indice operacional.
