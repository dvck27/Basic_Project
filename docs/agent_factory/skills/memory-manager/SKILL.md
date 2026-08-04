---
name: memory-manager
description: Mantiene un indice operacional ligero para agentes; usala para capturar notas reutilizables y punteros a los docs canonicos sin duplicar la verdad durable.
---

# Memory Manager

## Purpose
Mantener un indice operacional ligero y reutilizable para agentes, que acelere el trabajo repetido sin competir con los documentos canonicos del repositorio. La verdad durable del proyecto vive en `docs/`; este indice solo guarda hechos operacionales y punteros hacia esa verdad. No es un almacen de contexto duradero, ni un reemplazo de la documentacion oficial.

## Use When
- Un workflow repetido necesita una nota reutilizable (un paso, un atajo, una convencion operativa) que hoy hay que reconstruir cada vez.
- Una decision durable ya registrada necesita un puntero operacional que la haga facil de encontrar y aplicar en el dia a dia.
- Existe un hecho operacional estable y verificable que ayudara al trabajo futuro y que no cambia la verdad del proyecto.

## Do Not Use When
- La informacion es un secreto o credencial (tokens, contraseñas, claves, datos sensibles): nunca debe entrar al indice.
- La nota duplicaria contenido que ya vive en `docs/` sin agregar valor operacional; en ese caso enlaza al doc canonico en vez de copiarlo.
- Es un perfil personal, opinion no operativa o material externo crudo sin procesar.
- El contenido cambia la verdad durable del proyecto: eso pertenece a los docs canonicos, no al indice.

## Read First
Antes de escribir o modificar cualquier entrada, revisa los documentos canonicos relevantes para no duplicar ni contradecir la verdad durable:
- `docs/CONTEXT_PACK.md` — contexto durable del proyecto y su estado.
- `docs/DECISION_LOG.md` — decisiones durables y su justificacion.
- `docs/MAINTENANCE_CHECKLIST.md` — tareas de mantenimiento y convenciones operativas.
- `AGENTS.md` — instrucciones y reglas de operacion para agentes.

## Procedure
1. Captura solo el hecho operacional: la accion, el paso o el atajo concreto que se reutilizara. Deja fuera el contexto durable, las justificaciones extensas y cualquier narrativa que pertenezca a `docs/`.
2. Enlaza al doc canonico que posee el contexto durable. Cada entrada del indice debe apuntar por ruta al documento en `docs/` que sostiene la verdad detras de la nota (por ejemplo `docs/DECISION_LOG.md` o `docs/CONTEXT_PACK.md`).
3. Elimina duplicados en lugar de agregar notas casi identicas. Antes de crear una entrada nueva, busca notas existentes; si hay una parecida, consolidalas en una sola en vez de acumular variantes.
4. Redacta cualquier cosa sensible. Si una nota rozara un secreto, credencial o dato personal, reemplaza el valor por un puntero neutro (donde vive el secreto, quien lo gestiona) sin exponer el valor real.

## Validation
Una entrada es valida cuando ayuda al trabajo futuro pero no cambia la verdad del proyecto. Verifica que:
- Aporta valor operacional reutilizable y no es una copia de `docs/`.
- Incluye un puntero al doc canonico correspondiente cuando aplica.
- No contiene secretos, credenciales ni datos personales.
- No introduce ni redefine verdad durable; si lo hace, la informacion debe migrar a los docs canonicos.

## Memory Update
- Si cambia contexto durable del proyecto: actualiza `docs/CONTEXT_PACK.md` (y `docs/DECISION_LOG.md` si la decision es nueva o cambia). Los docs canonicos son la fuente de verdad; el indice operacional solo refleja o apunta a ellos.
- Si solo cambia un hecho operacional reutilizable (un atajo, un paso, una convencion de trabajo): actualiza la entrada correspondiente del indice operacional y asegura que su puntero al doc canonico siga siendo correcto.
- Regla general: la verdad durable se escribe primero en `docs/`; el indice operacional se actualiza despues para mantener el puntero vigente. Nunca dejes el indice como unica fuente de una verdad durable.

## Common Errors
- Copiar contexto durable al indice en vez de enlazarlo, generando dos fuentes que luego divergen.
- Acumular notas casi identicas en lugar de consolidarlas, degradando el valor del indice.
- Registrar secretos o datos sensibles por comodidad; siempre redactalos y apunta a donde se gestionan.
- Usar el indice para decisiones durables sin reflejarlas en `docs/DECISION_LOG.md`, dejando la verdad fuera de los docs canonicos.
