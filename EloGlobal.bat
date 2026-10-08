@echo off
rem Starts EloGlobal from the source folder (development). The store build starts with EloGlobal.exe.
cd /d "%~dp0"
if not exist "%~dp0runtime\.setup-ok" (
  echo First start: setting up the development runtime...
  call "%~dp0setup.bat"
  if not exist "%~dp0runtime\.setup-ok" exit /b 1
)
start "" "%~dp0runtime\pythonw.exe" -s "%~dp0main.py"
