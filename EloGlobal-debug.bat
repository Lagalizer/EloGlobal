@echo off
rem Same as EloGlobal.exe but keeps a console window open with all log messages (for bug reports).
cd /d "%~dp0"
if not exist "%~dp0runtime\python.exe" if exist "%~dp0setup.bat" call "%~dp0setup.bat"
"%~dp0runtime\python.exe" -s "%~dp0main.py" %*
pause
