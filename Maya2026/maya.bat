@echo off
set MAYA_PATH="C:\Program Files\Autodesk\Maya2026\bin\maya.exe"

:: add env variable
set MAYA_SCRIPT_PATH=%~dp0scripts;%MAYA_SCRIPT_PATH%
set PYTHONPATH=%~dp0scripts;%PYTHONPATH%
set XBMLANGPATH=%XBMLANGPATH%;%~dp0prefs\icon



start "" %MAYA_PATH%
exit