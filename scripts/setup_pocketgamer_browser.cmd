@echo off
chcp 65001 >nul
set PYTHONUTF8=1
set PYTHONUNBUFFERED=1
cd /d "%~dp0.."
echo PocketGamer browser setup
echo Complete the website verification in the dedicated Chrome window.
echo The browser profile stays local and is excluded from Git.
python collectors\pocketgamer.py --setup-browser --preset yesterday --limit 1 --out tmp\pocketgamer_browser_setup\industry_news\manual
set PG_SETUP_EXIT=%ERRORLEVEL%
echo.
echo Collector exited with code %PG_SETUP_EXIT%. See the result above.
pause
exit /b %PG_SETUP_EXIT%
