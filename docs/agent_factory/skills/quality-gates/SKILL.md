---
name: quality-gates
description: Define el conjunto minimo de pruebas y checks que realmente prueban un cambio; usar ante cambios de comportamiento o nuevas integraciones y produce un gate de validacion sin tooling innecesario.
---

# Quality Gates

## Purpose
Establecer el conjunto MINIMO de pruebas, checks y verificaciones que realmente demuestran que un cambio funciona, sin inventar herramientas ni dependencias que no existen en el repositorio. El objetivo es que cada cambio observable quede respaldado por la evidencia mas pequeña y relevante posible, priorizando el tooling ya presente.

## Use When
- Hubo un cambio de comportamiento en el sistema (nueva funcionalidad, correccion, ajuste de logica u output).
- Se agrega o modifica una integracion (servicio externo, contrato, formato de datos, interfaz).
- Se necesita definir el criterio de "hecho" verificable para una tarea antes de cerrarla.

## Do Not Use When
- No hubo ningun cambio observable (por ejemplo, edicion de comentarios, reordenamiento sin efecto, cambios de formato puramente cosmeticos).
- El trabajo es exclusivamente documental y no altera comportamiento del sistema.

## Read First
Consulta estos documentos canonicos antes de definir el gate, para no duplicar convenciones ni contradecir decisiones ya tomadas:
- `docs/CONTEXT_PACK.md` — estado del stack, tooling disponible y contexto operativo del repositorio.
- `docs/DECISION_LOG.md` — decisiones previas sobre pruebas, herramientas o alcance de validacion.
- `docs/MAINTENANCE_CHECKLIST.md` — checks recurrentes ya acordados que el gate debe respetar.
- `AGENTS.md` — reglas de operacion para agentes y limites de lo permitido en el repositorio.

## Procedure
1. **Identificar los tests mas pequeños relevantes.** Localiza las pruebas existentes que cubren directamente el area afectada. Prefiere el test unitario o de contrato mas acotado que ejercite el cambio; evita suites completas cuando un caso puntual ya lo prueba.
2. **Agregar smoke checks si faltan tests.** Si el area no tiene cobertura, define una verificacion minima (smoke check) que confirme que el cambio se comporta como se espera end-to-end en su camino principal. Documenta claramente que valida y como se ejecuta.
3. **Preferir el tooling existente antes que nuevas dependencias.** Usa las herramientas, scripts y comandos ya presentes en el repositorio. No introduzcas frameworks, librerias ni dependencias nuevas solo para validar; si algo parece imprescindible, registralo como propuesta en `docs/DECISION_LOG.md` en lugar de asumirlo.
4. **Documentar la validacion que no pudo automatizarse.** Cuando una parte del cambio solo pueda comprobarse manualmente, deja constancia explicita de los pasos seguidos, el resultado observado y por que no se automatizo.

> Nota importante (repositorio agnostico): si el repositorio aun no tiene stack, framework de pruebas ni tooling definido, NO inventes comandos ni herramientas. Define el gate como **pendiente y agnostico**: describe en lenguaje neutro que deberia probarse y bajo que criterio, y marca la automatizacion como bloqueada hasta que se decida el stack. Registra esa dependencia en `docs/DECISION_LOG.md`.

## Validation
El gate se considera correcto cuando:
- Cada cambio observable esta cubierto por el test o smoke check mas pequeño que realmente lo prueba.
- No se agrego tooling, dependencias ni comandos inexistentes o innecesarios.
- La validacion que no se pudo automatizar quedo documentada con pasos y resultado.
- Si el repositorio carece de stack/tests, el gate quedo definido como pendiente y agnostico, sin comandos inventados.

## Memory Update
- En `docs/`: registra el gate acordado y su alcance donde corresponda (por ejemplo, decisiones de cobertura o herramientas en `docs/DECISION_LOG.md`, y checks recurrentes en `docs/MAINTENANCE_CHECKLIST.md`). Actualiza `docs/CONTEXT_PACK.md` si el estado del tooling o del stack cambio.
- En el indice operacional: anota el estado de ejecucion del gate (que se corrio, que quedo pendiente, que se valido manualmente) para que la siguiente iteracion tenga trazabilidad, sin duplicar el contenido canonico de `docs/`.

## Common Errors
- Ejecutar suites completas o pesadas cuando un test acotado ya prueba el cambio.
- Inventar comandos o herramientas que no existen en el repositorio para "cumplir" el gate.
- Introducir dependencias nuevas sin registrarlas como decision en `docs/DECISION_LOG.md`.
- Cerrar la tarea sin documentar las validaciones manuales realizadas.
- Asumir un lenguaje o framework en un repositorio que aun es agnostico.
