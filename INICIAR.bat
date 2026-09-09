@echo off
setlocal
cd /d "%~dp0"
if not exist .venv\Scripts\python.exe (
  echo [PAI Auto] Creando entorno local...
  py -3.11 -m venv .venv 2>nul || python -m venv .venv
  if errorlevel 1 goto :error
)
.venv\Scripts\python.exe -m pip install -q --upgrade pip
.venv\Scripts\python.exe -m pip install -q -e ".[dev]"
if errorlevel 1 goto :error
echo [PAI Auto] Abriendo interfaz local...
.venv\Scripts\pai-auto.exe
exit /b 0
:error
echo.
echo No se pudo preparar PAI Auto. Verifica que Python 3.11 o superior este instalado.
pause
exit /b 1
