@echo off
cd /d "%~dp0"
echo Current dir: %cd% > debug_log.txt
echo. >> debug_log.txt

echo [1] Checking python.exe... >> debug_log.txt
if exist "python\python.exe" (
    echo   OK: python.exe found >> debug_log.txt
) else (
    echo   FAIL: python.exe not found >> debug_log.txt
    goto :done
)

echo [2] Python version... >> debug_log.txt
python\python.exe --version >> debug_log.txt 2>&1

echo [3] Checking python311._pth... >> debug_log.txt
type python\python311._pth >> debug_log.txt 2>&1

echo [4] Testing basic import... >> debug_log.txt
python\python.exe -c "import sys; print(sys.path)" >> debug_log.txt 2>&1

echo [5] Testing site-packages import... >> debug_log.txt
python\python.exe -c "import torch; print('torch OK')" >> debug_log.txt 2>&1

echo [6] Testing pocket_tts import... >> debug_log.txt
python\python.exe -c "from pocket_tts import TTSModel; print('pocket_tts OK')" >> debug_log.txt 2>&1

echo [7] Checking model files... >> debug_log.txt
if exist "models\model.safetensors" (
    echo   OK: model.safetensors found >> debug_log.txt
) else (
    echo   FAIL: model.safetensors missing >> debug_log.txt
)
if exist "models\tokenizer.model" (
    echo   OK: tokenizer.model found >> debug_log.txt
) else (
    echo   FAIL: tokenizer.model missing >> debug_log.txt
)

:done
echo. >> debug_log.txt
echo === Done. Check debug_log.txt for results. === >> debug_log.txt
type debug_log.txt
echo.
echo Results above also saved to debug_log.txt
pause
