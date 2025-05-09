@echo off
set SUBSTANDEPAINTER_PATH="C:\Program Files\Adobe\Adobe Substance 3D Painter\Adobe Substance 3D Painter.exe"
set "SHELF_PATH=%~dp0shelf"

:: add env variable
set OCIO=%~dp0OCIO\simple.config.ocio

set "SOURCE_PATH=%~dp0export-presets"
set "TARGET_PATH=%USERPROFILE%\Documents\Adobe\Adobe Substance 3D Painter\assets\export-presets"
xcopy "%SOURCE_PATH%\*" "%TARGET_PATH%\" /E /H /Y

start "" %SUBSTANDEPAINTER_PATH%
exit