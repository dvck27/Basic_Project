---
name: readme-maintainer
description: Alinea el README con el comportamiento real del repositorio; usala cuando cambian instalacion, arranque, pruebas, build, lint, entrypoints, URLs/puertos, flujos o dependencias, y produce un README verificable, conciso y accionable.
---

# Mantenimiento del README (readme-maintainer)

## Purpose
Mantener el README como reflejo fiel del comportamiento **real** del repositorio.

Principio rector: **documenta solo lo verificable**. Toda afirmacion del README debe
poder comprobarse en el codigo o la configuracion presentes en el repositorio. Lo que
no puedas verificar se marca explicitamente como `No verificado` o `Por definir`, nunca
se inventa ni se asume.

Este repositorio es una base **agnostica**: no asumas ningun lenguaje, framework,
gestor de paquetes ni runtime. Deriva cada dato del README de la evidencia concreta que
encuentres, no de convenciones tipicas de un stack.

## Use When
Ejecuta esta skill cuando exista evidencia en codigo o configuracion de que cambio algo
de lo que el README describe, por ejemplo:

- Cambian los pasos de instalacion o preparacion del entorno.
- Cambian los comandos de arranque, prueba (test), build o lint.
- Cambia el o los entrypoints del proyecto.
- Cambian URLs, puertos, hosts o rutas expuestas.
- Cambian flujos de uso, pasos operativos o el orden de ejecucion.
- Cambian dependencias, requisitos previos o variables de configuracion.

## Do Not Use When
- No hay evidencia del cambio en el codigo o la configuracion (un cambio solo mencionado
  de palabra, sin respaldo en el repositorio, no es evidencia).
- El cambio es puramente interno y no altera nada de lo que el README describe al lector.
- La informacion que se pide agregar no puede verificarse (en ese caso, o se marca como
  `No verificado` / `Por definir`, o no se agrega).

## Read First
Antes de editar el README, revisa los documentos canonicos para conocer el contexto, las
decisiones vigentes y las convenciones del repositorio:

- `docs/CONTEXT_PACK.md` — contexto general del repositorio y su proposito.
- `docs/DECISION_LOG.md` — decisiones tomadas y su justificacion (evita contradecirlas).
- `docs/MAINTENANCE_CHECKLIST.md` — pasos de mantenimiento y verificacion esperados.
- `AGENTS.md` — convenciones para agentes y limites de actuacion en este repositorio.

Ademas, inspecciona la fuente real de la que dependen las afirmaciones del README:
archivos de configuracion, scripts, manifiestos, definiciones de tareas y el o los
entrypoints reales del proyecto.

## Procedure
1. **Verificar el comportamiento real desde el codigo/config.**
   Localiza y lee los archivos que definen instalacion, arranque, pruebas, build, lint,
   entrypoints, puertos/URLs, flujos y dependencias. Cada dato que vayas a escribir debe
   tener una fuente concreta en el repositorio. Si un dato no aparece en ningun lado,
   trátalo como desconocido.

2. **Actualizar solo las secciones afectadas.**
   Modifica unicamente las partes del README que el cambio verificado vuelve incorrectas
   o incompletas. No reescribas secciones que siguen siendo correctas.

3. **No afirmar lo inexistente.**
   No declares CI/CD, licencia, despliegue, integraciones ni herramientas que no existan
   de forma verificable en el repositorio. Si algo es necesario pero no esta definido,
   márcalo como `No verificado` o `Por definir` en lugar de omitirlo silenciosamente o
   inventarlo.

4. **Mantener el README conciso y accionable.**
   Prioriza pasos claros que un mantenedor pueda seguir. Evita relleno, promesas y
   descripciones aspiracionales. Nunca incluyas secretos, credenciales, tokens ni valores
   sensibles; usa marcadores (por ejemplo `<VARIABLE>`) cuando haga falta ilustrar.

## Validation
El cambio es correcto cuando **un mantenedor nuevo, sin conocimiento previo del proyecto,
puede instalar, ejecutar y probar el proyecto siguiendo unicamente el README** y obtiene
el comportamiento real observado en el repositorio.

Verifica ademas que:
- Cada comando o paso del README corresponde a algo que existe en el codigo/config.
- No queda ninguna afirmacion sobre CI/CD, licencia, despliegue o herramientas sin
  respaldo real.
- Lo desconocido esta marcado como `No verificado` o `Por definir`, no adivinado.
- No se filtraron secretos ni valores sensibles.

## Memory Update
- **En `docs/`**: si el cambio del README refleja o implica una decision de fondo (por
  ejemplo, nuevo entrypoint, nuevo flujo operativo, cambio de puertos o de dependencias
  con impacto), registra la decision en `docs/DECISION_LOG.md` y actualiza
  `docs/CONTEXT_PACK.md` si cambia el contexto general. Ajusta
  `docs/MAINTENANCE_CHECKLIST.md` si cambian los pasos de mantenimiento o verificacion.
- **En el indice operacional**: actualiza la entrada correspondiente al README (fecha,
  alcance del cambio y motivo) para dejar trazabilidad de que el README quedo alineado
  con el estado real del repositorio.

## Common Errors
- Copiar comandos o rutas de otro stack por costumbre en vez de derivarlos del repositorio.
- Documentar el comportamiento deseado en lugar del comportamiento real y verificable.
- Eliminar los marcadores `No verificado` / `Por definir` sin haber verificado el dato.
- Reescribir el README completo cuando solo una seccion cambio.
