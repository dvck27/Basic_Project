@echo off
setlocal
cd /d "%~dp0"
if not exist .venv\Scripts\python.exe (
  echo Primero ejecuta INICIAR.bat una vez.
  pause
  exit /b 1
)
echo [PAI Auto] Instalando integraciones reales...
.venv\Scripts\python.exe -m pip install -e ".[real]"
if errorlevel 1 goto :error
.venv\Scripts\python.exe -m playwright install chromium
if errorlevel 1 goto :error
echo.
echo Preparacion terminada. El modo PAIWEB real ya dispone de Playwright y Gmail OAuth.
pause
exit /b 0
:error
echo.
echo No se pudo completar la preparacion del modo real.
pause
exit /b 1
