# PAI Auto

PAI Auto es una versión compacta y local-first del flujo aprendido en `dvck27/vacunacion-paiweb`.
Su objetivo es simple: **leer el Registro Diario SIS, descomponer cada fila en aplicaciones PAI,
validarlas, ejecutarlas por una fila o lotes de 20/50/100 filas, verificar el resultado y dejar
trazabilidad local**.

La aplicación está pensada para un **único administrador**. No replica comités, roles, gates ni la
arquitectura extensa del repositorio de investigación. Mantiene únicamente las defensas que afectan
la consistencia del dato: contrato del Excel, no inventar campos, idempotencia, verificación posterior
y continuidad del lote ante fallos individuales.

## Estado de esta entrega

- ✅ Flujo end-to-end contra simulador local.
- ✅ Importación del formato de 222 columnas (`Vacunación SIS`, datos desde fila 16).
- ✅ Descomposición de los 28 grupos PAI de `BN:FF`; una fila puede producir varias aplicaciones.
- ✅ Selección por **filas fuente**: 1, 20, 50 o 100; se incluyen todas las aplicaciones válidas de cada fila.
- ✅ SQLite local para ejecuciones, resultados e idempotencia.
- ✅ Interfaz web minimalista para un administrador único.
- ✅ Adaptador Playwright para login → OTP → sede → paciente → esquema → formulario → guardar → verificar.
- ✅ OTP por Gmail OAuth con alcance `gmail.readonly`.
- ⚠️ El modo real debe validarse primero con **una fila**. El repositorio original logró recorridos reales
  de lectura, pero no había ejecutado una escritura real; por eso esta entrega no afirma que los selectores
  de guardado estén validados en producción.
- ⏳ Biológicos particulares `FG:HJ`, alta de pacientes nuevos y un LLM local están fuera de la V0.

## Stack

- Python 3.11+
- FastAPI + Jinja2 (UI local)
- SQLite (stdlib)
- openpyxl (Excel)
- Playwright/Chromium (modo PAIWEB real, opcional)
- Gmail API OAuth readonly (OTP, opcional)

No requiere Django, Redis, Docker, SQL Server ni un servidor externo.

## Arranque rápido — simulador

### Windows

Ejecuta `INICIAR.bat`. La primera vez crea `.venv`, instala el proyecto y abre:

`http://127.0.0.1:8765`

### Manual

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install -e ".[dev]"
.venv\Scripts\pai-auto.exe
```

En Linux/macOS cambia `Scripts` por `bin`.

## Preparar modo PAIWEB real

En Windows ejecuta una vez:

```powershell
PREPARAR_REAL.bat
```

Equivale a instalar `.[real]` y Chromium de Playwright. Las credenciales de PAIWEB y el token OAuth
**no se guardan en Git**. Se suministran al iniciar la corrida y la contraseña no se persiste en SQLite.

El modo real exige además cuatro valores operativos explícitos para el lote: número de unidades,
sitio anatómico, tipo de aplicación y sector económico. No hay valores clínicos/administrativos
implícitos para escritura real.

### Límite de pruebas reales

Por defecto:

```text
PAI_AUTO_REAL_MAX_ROWS=1
```

Después de validar la primera escritura real, el administrador puede habilitar un lote mayor antes de
arrancar la aplicación, por ejemplo en PowerShell:

```powershell
$env:PAI_AUTO_REAL_MAX_ROWS="20"
.venv\Scripts\pai-auto.exe
```

Admite hasta 100 filas porque los tamaños de lote de la UI son `1/20/50/100`.

## Flujo

```text
XLSX
  → validar estructura
  → descomponer fila en aplicaciones PAI
  → filtrar incidencias
  → seleccionar 1/20/50/100 filas
  → comprobar idempotencia
  → escribir (simulador o PAIWEB)
  → verificar
  → marcar procesado
  → continuar
  → informe local
```

Una aplicación fallida **no detiene las demás**. Una aplicación solo se marca como procesada después
de que el gateway confirme la verificación posterior.

## Portabilidad

La aplicación y sus datos operativos viven en una carpeta:

```text
Basic_Project/
├── src/pai_auto/
├── runtime/
│   ├── pai_auto.db
│   └── uploads/
├── INICIAR.bat
└── PREPARAR_REAL.bat
```

`runtime/`, `.venv/`, credenciales y tokens están ignorados por Git. Esta V0 usa un entorno Python local;
un empaquetado posterior con PyInstaller puede convertirla en una distribución portable sin cambiar el
motor de workflow.

## Pruebas y calidad

```powershell
.venv\Scripts\python.exe -m pytest
.venv\Scripts\ruff.exe check .
```

Cobertura inicial: importación sintética de 222 columnas, lotes contados por fila, recorrido completo del
simulador e idempotencia.

## Principio del LLM

Un LLM local podrá incorporarse después como un nodo opcional para diagnóstico, explicación de errores o
normalización no clínica. **No estará en el camino que decide identidad, biológico, dosis, lote ni campos
clínicos**; esos valores continúan siendo determinísticos.

Consulta `specs/WORKFLOW.md` y `docs/agent_factory/prps/pai-auto-v0.md` para el contrato de esta versión.
