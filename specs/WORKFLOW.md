# Contrato funcional — PAI Auto v0

## Objetivo
Procesar localmente el Registro Diario SIS de 222 columnas y ejecutar aplicaciones PAI por una fila o lotes de 20, 50 o 100 **filas fuente**, con un único administrador.

## Flujo
1. Leer `Vacunación SIS`, datos desde fila 16, 222 columnas exactas.
2. Descomponer `BN:FF` en aplicaciones PAI. Una fila puede producir varias aplicaciones.
3. Bloquear un grupo con datos sin dosis/frascos o con lote ausente.
4. Seleccionar desde una fila de origen y tomar 1/20/50/100 **filas fuente**, incluyendo todas las aplicaciones válidas de esas filas.
5. Calcular una huella idempotente por tipo/número de documento + fecha + código/tipo de biológico + dosis + lote.
6. Si la huella ya fue confirmada, omitirla.
7. Escribir mediante `SimulatorGateway` o `PaiwebBrowserGateway`.
8. Verificar después de escribir. Solo entonces marcar la huella como procesada.
9. Un fallo de una aplicación no detiene las siguientes del lote.
10. Guardar ejecución e ítems en SQLite local.

## Administrador único
No existen roles ni firmas distribuidas. El administrador decide cuándo ejecutar y suministra en modo real los valores que PAIWEB exige y el libro no contiene (`units`, `anatomical_site`, `application_type`, `economic_sector`). No existen valores implícitos para esos cuatro campos en una escritura real y un LLM nunca los decide.

La aprobación humana ocurre **una sola vez por corrida**, antes de empezar. Luego el lote es desatendido salvo fallos no recuperables de sesión.

## Tamaño de lote
El tamaño se cuenta por `source_row`, no por aplicaciones. Si una de 20 filas contiene tres biológicos, los tres pertenecen al mismo lote y deben procesarse.

Valores admitidos: `1`, `20`, `50`, `100`.

## Modos
- `simulator`: recorrido completo sin tocar PAIWEB.
- `real`: navegador Playwright + OTP Gmail readonly + sede + búsqueda de paciente + línea de esquema + formulario + Guardar + confirmación + verificación.

## Escritura real
- Requiere checkbox de confirmación del administrador.
- Requiere credenciales, sede y referencia local al token Gmail OAuth.
- Requiere valores explícitos para unidades, sitio anatómico, tipo de aplicación y sector económico.
- `PAI_AUTO_REAL_MAX_ROWS` limita filas reales por ejecución; default `1`. Puede configurarse a 20/50/100 después de validar una fila.
- La contraseña no se persiste.

## Fuente de verdad PAIWEB
Los nombres de biológico y selectores iniciales proceden del levantamiento/mapeo 2026 de `vacunacion-paiweb`. Algunos literales de biológico siguen siendo propuestas del proyecto original, no una garantía contractual de PAIWEB; cualquier divergencia debe producir fallo de la aplicación, nunca coincidencia difusa.

## Restricciones v0
- Solo biológicos PAI `BN:FF`; `FG:HJ` (particulares) no se envían.
- No registra pacientes nuevos.
- No automatiza autorizaciones clínicas, solicitudes de cambio ni correcciones de expedientes.
- No usa coincidencia difusa para identidad, dosis o lote.
- Un LLM queda fuera del camino crítico; podrá agregarse como nodo opcional sin producir datos clínicos.
- La primera escritura real aún debe validarse: el repositorio original no había ejecutado una escritura real.
