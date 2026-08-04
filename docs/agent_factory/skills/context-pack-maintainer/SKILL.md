---
name: context-pack-maintainer
description: Usala cuando cambie algo duradero del proyecto (proposito, arquitectura, entrypoints, memoria, orden de lectura, dependencias, publicacion o riesgos); produce un docs/CONTEXT_PACK.md compacto y exacto para retomar en un chat nuevo.
---

# Mantenedor del Context Pack

## Purpose
Mantener `docs/CONTEXT_PACK.md` compacto, exacto y util para garantizar continuidad entre sesiones. El Context Pack es el resumen minimo y de alta senal que permite a un agente nuevo entender el proyecto y retomar el trabajo sin adivinar ni releer todo el repositorio. Esta skill no crea conocimiento nuevo: refleja el estado real del repositorio y remite a las fuentes de verdad canonicas.

## Use When
Actualiza el Context Pack cuando cambie cualquier hecho duradero del proyecto, por ejemplo:
- El **proposito** o alcance del proyecto.
- La **arquitectura** o los componentes principales.
- Los **entrypoints** (como se arranca, se prueba o se opera el proyecto).
- La **estructura** de carpetas o la ubicacion de los artefactos importantes.
- El **modelo de memoria** (que persiste en `docs/` frente a memoria runtime u operacional).
- El **orden de lectura** recomendado para entender el proyecto.
- Las **dependencias criticas** o servicios externos de los que depende el trabajo.
- La **configuracion durable** (parametros estables, no secretos, no valores efimeros).
- El **flujo de publicacion** o entrega.
- Los **riesgos duraderos** o restricciones conocidas.

## Do Not Use When
No actualices el Context Pack cuando:
- El cambio es **efimero** (estado temporal, resultados de una sola sesion, notas de trabajo en curso).
- La informacion pertenece a **memoria runtime u operacional** (progreso de tareas, TODOs del dia, hallazgos transitorios) que vive en el indice operacional, no en el Context Pack.
- Se trata de una **decision de diseno** con su justificacion: eso se registra en `docs/DECISION_LOG.md`; en el Context Pack solo dejas el hecho resultante si es duradero.
- Estas ante un detalle de bajo nivel que **no cambia como se retoma el proyecto** en un chat nuevo.

## Read First
Antes de editar, lee y respeta la jerarquia de fuentes de verdad:
- `docs/CONTEXT_PACK.md` — el archivo que vas a mantener; entiende su estructura actual antes de tocarlo.
- `AGENTS.md` — reglas y convenciones para agentes; el Context Pack debe ser coherente con ellas.
- `docs/DECISION_LOG.md` — decisiones y su justificacion; consulta si un cambio arquitectonico ya quedo decidido.
- `docs/MAINTENANCE_CHECKLIST.md` — pasos de mantenimiento y verificacion asociados a los docs canonicos.

## Procedure
1. **Verificar el estado real.** Contrasta lo que dice el Context Pack contra el repositorio actual (estructura, entrypoints, dependencias, flujo de publicacion). No documentes intenciones ni suposiciones: documenta lo que existe y es verificable.
2. **Actualizar solo las secciones afectadas.** Edita unicamente las secciones del Context Pack que cambiaron. Manten el documento compacto: elimina lo obsoleto, evita duplicar contenido que ya vive en otros docs canonicos y enlaza a ellos en lugar de copiarlo.
3. **Mantener la jerarquia de fuentes de verdad y el "como retomar en un chat nuevo".** Conserva el orden de lectura y la seccion que explica como un agente nuevo debe arrancar. Cada afirmacion debe apuntar, cuando corresponda, a su fuente canonica (`AGENTS.md`, `docs/DECISION_LOG.md`, `docs/MAINTENANCE_CHECKLIST.md`).
4. **Declarar gaps.** Si hay informacion desconocida, no verificada o pendiente, decláralo explicitamente como gap en lugar de inventar. Un gap declarado es mas util que un dato falso.

## Validation
El Context Pack esta bien mantenido si un **agente nuevo puede retomar el trabajo leyendolo, sin adivinar**:
- El proposito, la arquitectura y los entrypoints quedan claros y coinciden con el estado real.
- El orden de lectura y el "como retomar en un chat nuevo" permiten arrancar sin explorar a ciegas.
- No hay contradicciones entre el Context Pack y `AGENTS.md`, `docs/DECISION_LOG.md` o `docs/MAINTENANCE_CHECKLIST.md`.
- Los gaps estan declarados; no hay datos inventados ni secretos incluidos.
- El documento sigue siendo compacto: alta senal, sin relleno ni duplicacion.

## Memory Update
- **En `docs/` (memoria durable):** actualiza `docs/CONTEXT_PACK.md` con los hechos duraderos. Si el cambio nace de una decision con justificacion, registra la decision en `docs/DECISION_LOG.md` y refleja solo el hecho resultante en el Context Pack. Ajusta `docs/MAINTENANCE_CHECKLIST.md` si el mantenimiento cambia.
- **En el indice operacional (memoria runtime):** deja alli el progreso, los TODOs y el estado transitorio. Nunca muevas ese contenido efimero al Context Pack; el Context Pack solo contiene lo que sigue siendo cierto entre sesiones.

## Common Errors
- Copiar en el Context Pack contenido que ya vive en otro doc canonico en vez de enlazarlo (rompe la fuente unica de verdad).
- Documentar planes o intenciones en lugar del estado real y verificable.
- Mezclar memoria runtime (efimera) con memoria durable.
- Dejar el documento crecer sin podar lo obsoleto, perdiendo compacidad.
- Inventar datos para evitar declarar un gap.
