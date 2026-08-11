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
echo The browser will open automatically when the server is ready.
echo Press Ctrl+C to stop.
echo.
echo ==========================================
echo.

python\python.exe pocket_tts_api.py

echo.
echo Pocket TTS has stopped.
pause
