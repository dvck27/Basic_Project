---
name: decision-log
description: Registra decisiones tecnicas durables en docs/DECISION_LOG.md cuando cambia arquitectura, seguridad, testing, proveedores, estructura del repo o el contrato de agentes; produce una entrada trazable con contexto, decision, motivo e impacto.
---

# Decision Log

## Purpose
Mantener un registro cronologico y auditable de las decisiones tecnicas **durables** del repositorio en `docs/DECISION_LOG.md`. El objetivo es que cualquier persona o agente que llegue mas tarde entienda **por que** existe una decision, **que afecto** y **que alternativas se descartaron**, sin tener que reconstruir el razonamiento a partir del historial de cambios. Es la memoria de "por que hicimos esto asi".

## Use When
Registra una entrada cuando la decision tiene efecto duradero sobre el proyecto, por ejemplo:
- Cambios en la **arquitectura** o en como se organizan los componentes.
- Cambios en **persistencia** (modelo de datos, almacenamiento, esquema).
- Decisiones de **seguridad** (autenticacion, autorizacion, manejo de secretos, superficie expuesta).
- Estrategia o convenciones de **testing**.
- Eleccion o cambio de **proveedores / costos** (servicios externos, dependencias con impacto economico o de dependencia).
- Cambios en la **estructura del repositorio** (carpetas, convenciones, ubicacion de docs).
- Cambios que afecten el **onboarding** de nuevas personas o agentes.
- **Migraciones** de datos, formatos o versiones.
- Decisiones de **compatibilidad** (versiones soportadas, contratos de interfaz, rupturas hacia atras).
- Cambios en el **contrato de agentes** (lo definido en `AGENTS.md`).
- Cambios en el **flujo de publicacion** (como se libera, valida o distribuye el trabajo).

Regla practica: si dentro de seis meses alguien podria preguntar "por que esta hecho asi?", registra la decision.

## Do Not Use When
No registres una entrada cuando el cambio es **trivial** o reversible sin consecuencias, por ejemplo:
- Correcciones menores de redaccion, formato o typos.
- Renombrados locales sin impacto en contratos ni en la estructura publica.
- Ajustes cosmeticos que no cambian comportamiento ni convenciones.
- Cambios exploratorios o temporales que aun no son una decision consolidada.

Si tienes dudas y la decision es facil de deshacer sin afectar a nadie mas, no la registres. El log debe permanecer denso en senal.

## Read First
Antes de escribir una entrada, revisa los documentos canonicos relevantes para dar contexto correcto y evitar duplicar informacion:
- `docs/DECISION_LOG.md` — el propio registro; revisa el formato y las entradas recientes.
- `docs/CONTEXT_PACK.md` — estado y contexto general del proyecto; verifica si la decision cambia algo que alli se describe.
- `AGENTS.md` — contrato de agentes; obligatorio de revisar si la decision toca dicho contrato.
- `docs/MAINTENANCE_CHECKLIST.md` — comprueba si la decision introduce una nueva tarea de mantenimiento recurrente.

## Procedure
1. Confirma que la decision cae dentro de **Use When** y no dentro de **Do Not Use When**.
2. Abre `docs/DECISION_LOG.md`.
3. Agrega una **nueva entrada al principio** (la mas reciente arriba, orden cronologico descendente).
4. Usa exactamente este encabezado y estos campos:

   ```markdown
   ## YYYY-MM-DD - Titulo breve de la decision

   - **Contexto:** situacion o problema que motivo la decision.
   - **Decision:** que se decidio hacer, en una o dos frases claras.
   - **Motivo:** por que esa opcion y no otra.
   - **Impacto:** que cambia como consecuencia (componentes, flujos, personas afectadas).
   - **Alternativas consideradas:** opciones evaluadas y por que se descartaron.
   - **Documentos/codigo afectados:** rutas de docs o areas del repositorio que cambian o deben cambiar.
   ```

5. Usa la fecha real del dia en formato `YYYY-MM-DD`.
6. Manten cada campo **breve y directo**: frases concretas, no narrativa extensa. Una entrada larga suele indicar que hay que dividir la decision o resumir mas.
7. Si la decision afecta a otro documento canonico (por ejemplo `AGENTS.md` o `docs/CONTEXT_PACK.md`), actualiza tambien ese documento en el mismo cambio.

## Validation
Una entrada esta bien hecha cuando:
- Deja claro **por que existe la decision**, no solo que se hizo.
- Indica sin ambiguedad **que afecto** (documentos, areas del repo, flujos).
- Sigue el encabezado `## YYYY-MM-DD - Titulo` y contiene los seis campos.
- Aparece **arriba** de las entradas anteriores (mas reciente primero).
- Es **breve**: se puede leer y entender en menos de un minuto.
- No contiene secretos, credenciales ni datos sensibles.
- Los documentos referenciados en "Documentos/codigo afectados" fueron actualizados si la decision lo requeria.

## Memory Update
- En `docs/`: la fuente de verdad de la decision vive en `docs/DECISION_LOG.md`. Si la decision cambia el estado del proyecto, refleja el resultado (no la deliberacion) en `docs/CONTEXT_PACK.md`; si cambia el contrato de agentes, actualiza `AGENTS.md`; si crea mantenimiento recurrente, agrega la tarea en `docs/MAINTENANCE_CHECKLIST.md`.
- En el indice operacional: solo registra el puntero minimo necesario (fecha y titulo de la decision) para poder localizarla. El indice operacional apunta al log, no lo reemplaza ni duplica su contenido.

## Common Errors
- Escribir narrativa larga en lugar de campos breves y accionables.
- Agregar la entrada al final del archivo en vez de arriba (rompe el orden cronologico descendente).
- Registrar cambios triviales, diluyendo la senal del log.
- Omitir "Alternativas consideradas", que es lo que da valor futuro a la decision.
- Actualizar el log pero olvidar sincronizar el documento canonico afectado.
