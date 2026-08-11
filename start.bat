@echo off
cd /d "%~dp0"

echo.
echo ==========================================
echo   Pocket TTS - Offline Portable
echo ==========================================
echo.
echo Current directory: %cd%
echo.

:: Check: are we extracted?
if not exist "python\python.exe" (
    echo [ERROR] python\python.exe not found.
    echo.
    echo Make sure you EXTRACTED the zip file first.
    echo Do NOT run start.bat from inside the zip.
    echo.
    echo Current files in this folder:
    dir /b
    echo.
    pause
    exit /b 1
)

:: Check: do we have the model?
if not exist "models\model.safetensors" (
    echo [ERROR] models\model.safetensors not found.
    echo The model files are missing. Make sure you extracted the entire zip.
    echo.
    pause
    exit /b 1
)

:: Set offline mode
set HF_HUB_OFFLINE=1
set HF_DATASETS_OFFLINE=1
set TRANSFORMERS_OFFLINE=1
set NO_COLOR=1

echo Starting Pocket TTS server...
echo Model loading - this may take 30-60 seconds on first run.
echo.
echo Model loading - this may take 30-60 seconds on first run.
echo The browser will open automatically when ready.
echo Press Ctrl+C to stop.
echo.
echo ==========================================
echo.

:: Launch server in background, wait for it to be ready, then open browser
start "" /B python\python.exe pocket_tts_api.py

:: Poll health endpoint until server is ready (max 120 seconds)
echo Waiting for server to start...
for /L %%i in (1,1,120) do (
    powershell -Command "try { $r = Invoke-WebRequest -Uri 'http://localhost:8000/health' -UseBasicParsing -TimeoutSec 1; exit 0 } catch { exit 1 }" >nul 2>&1
    if %errorlevel% equ 0 (
        echo Server ready! Opening browser...
        start http://localhost:8000
        goto :server_running
    )
    timeout /t 1 /nobreak >nul
)
echo Server did not start within 120 seconds.
goto :end

:server_running
echo.
echo Pocket TTS is running. Close this window to stop.
echo.
:: Wait for the python process to exit
:waitloop
timeout /t 5 /nobreak >nul
tasklist /FI "IMAGENAME eq python.exe" 2>nul | find /I "python.exe" >nul
if %errorlevel% equ 0 goto :waitloop

:end
echo Pocket TTS has stopped.
pause
