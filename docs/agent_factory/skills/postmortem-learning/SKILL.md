---
name: postmortem-learning
description: Convierte un fallo o incidente en un control de ingenieria durable (regla + test de regresion + documentacion). Usala cuando un fix se repite, un workflow confunde, o un fallo deberia volverse regla.
---

# Postmortem Learning

## Purpose
Transformar un fallo, incidente o confusion recurrente en un control de ingenieria durable. El resultado no es un relato del problema, sino tres artefactos concretos que evitan que el fallo se repita:

- una **regla de prevencion** explicita,
- un **test de regresion** que reconoce el fallo de forma determinista,
- **documentacion sincronizada** con el comportamiento real.

El objetivo es que el aprendizaje quede en el sistema (repositorio, tests, docs) y no solo en la memoria de una persona o en un chat.

## Use When
Aplica esta skill cuando ocurre alguna de estas situaciones:

- Un **fix se repite**: el mismo error se corrige mas de una vez o vuelve tras "arreglarse".
- Un **workflow confunde**: un procedimiento produce resultados inesperados o requiere conocimiento tribal para no equivocarse.
- Un **fallo deberia volverse regla**: hubo un incidente cuya prevencion puede codificarse como control reutilizable.
- Se detecta una **causa raiz reutilizable**: la leccion aplica a mas casos que el incidente puntual.

## Do Not Use When
No apliques esta skill cuando:

- El **evento es trivial** y no deja ninguna leccion reutilizable (por ejemplo, un typo aislado ya corregido sin patron).
- El **material contiene secretos sin redactar** (credenciales, tokens, datos personales, rutas internas sensibles). Primero redacta; solo entonces documenta.
- Todavia **no hay evidencia suficiente** para distinguir hechos de suposiciones. En ese caso, primero recolecta datos; no escribas conclusiones prematuras.

## Read First
Antes de escribir el postmortem, revisa los documentos canonicos del repositorio para alinear terminologia, decisiones previas y procedimientos:

- `AGENTS.md` — convenciones de trabajo y expectativas para agentes y colaboradores.
- `docs/CONTEXT_PACK.md` — contexto operativo del proyecto y estado vigente; verifica si el incidente contradice algo ya documentado.
- `docs/DECISION_LOG.md` — decisiones tomadas y su justificacion; comprueba si la causa raiz choca con una decision previa o exige una nueva.
- `docs/MAINTENANCE_CHECKLIST.md` — tareas de mantenimiento y verificaciones periodicas; evalua si la regla nueva debe incorporarse aqui.

Si existen specs o runbooks especificos del area afectada, leelos tambien antes de proponer cambios.

## Procedure
Sigue los pasos en orden. Cada paso produce evidencia o un artefacto verificable.

1. **Declarar sintoma e impacto visible.** Describe que se observo (no que se supone) y a quien o que afecto: quien lo noto, alcance, severidad y ventana temporal. El sintoma debe ser reconocible por alguien externo.

2. **Construir una linea de tiempo factual.** Ordena cronologicamente los hechos con su evidencia: comandos ejecutados, salidas de logs, diffs, cambios de configuracion y eventos externos. Cada entrada debe apuntar a una fuente verificable, no a memoria.

3. **Separar hechos, hipotesis descartadas e incertidumbre.** Distingue de forma explicita tres categorias: hechos confirmados por evidencia; hipotesis que se probaron y se descartaron (con el porque); y zonas de incertidumbre que quedan abiertas. No mezcles suposicion con hecho.

4. **Identificar causa raiz y contribuyentes.** Determina la causa raiz (la condicion cuya ausencia habria evitado el fallo) y sepArala de los factores contribuyentes que la agravaron o facilitaron. Evita quedarte en el sintoma.

5. **Definir la regla de prevencion.** Formula una regla clara, accionable y verificable que evite la reaparicion. Debe poder comprobarse de forma objetiva (no un buen deseo). Indica donde vive esa regla (checklist, spec, configuracion, control automatizado).

6. **Agregar test de regresion.** Escribe una prueba que falle ante el fallo original y pase tras el fix. El test debe reconocer el problema de forma determinista y **no debe mutar el estado real del usuario** (usa entornos aislados, fixtures o datos de prueba; nunca datos productivos ni credenciales reales).

7. **Sincronizar documentacion.** Actualiza los documentos afectados para que coincidan con el comportamiento real: la spec o runbook del area, `docs/CONTEXT_PACK.md`, y `docs/DECISION_LOG.md` si la causa raiz implica o revierte una decision. Si la regla es periodica, refleja el control en `docs/MAINTENANCE_CHECKLIST.md`.

8. **Guardar el reporte en docs/.** Persiste el postmortem completo (sintoma, linea de tiempo, causa raiz, regla, test, cambios de docs) como archivo en `docs/`. El aprendizaje debe vivir en el repositorio, no en el chat.

## Validation
El postmortem esta completo cuando se cumplen las tres condiciones:

- **Reconocimiento determinista.** El fallo original se reproduce y se detecta de forma consistente; el test de regresion falla sin el fix y pasa con el.
- **Fix reproducible.** Cualquier persona puede aplicar el arreglo siguiendo el reporte y obtener el mismo resultado, sin conocimiento tacito adicional.
- **Docs coinciden con el comportamiento.** La documentacion actualizada describe lo que el sistema hace realmente; no quedan contradicciones entre reporte, regla, test y docs canonicos.

## Memory Update
Distingue entre memoria durable (en `docs/`) y el indice operacional:

- **En `docs/` (memoria durable):**
  - Guarda el reporte de postmortem como archivo persistente en `docs/`.
  - Actualiza `docs/CONTEXT_PACK.md` con el nuevo estado o comportamiento si cambio.
  - Registra en `docs/DECISION_LOG.md` toda decision que la causa raiz haya originado o revertido, con su justificacion.
  - Incorpora el control periodico en `docs/MAINTENANCE_CHECKLIST.md` cuando la regla requiera verificacion recurrente.
- **En el indice operacional (referencia rapida):**
  - Enlaza el nuevo reporte desde el indice de postmortems o desde donde el equipo consulte lecciones aprendidas, para que sea descubrible.
  - Anota la regla y el test asociados junto al area afectada, de modo que futuras tareas los encuentren sin releer todo el reporte.

## Common Errors
Evita estos patrones frecuentes que degradan el valor del postmortem:

- **Documentar conclusiones sin evidencia.** Escribir la causa raiz o la regla sin respaldarlas en la linea de tiempo factual; toda afirmacion debe apuntar a evidencia.
- **Tratar el sintoma como causa raiz.** Detenerse en lo observable (el error visible) sin llegar a la condicion que lo provoco, con lo que el fallo reaparece por otra via.
- **Guardar el incidente solo en el chat.** Dejar el aprendizaje en una conversacion efimera en lugar de persistirlo en `docs/`, en un test y en una regla verificable.
