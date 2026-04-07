@echo off
echo Starting Pakistan Sales Tracker Dashboard...
echo Close this window to stop the server.
echo.
echo Dashboard will open at http://localhost:8000
start http://localhost:8000
python -m http.server 8000
pause
