@echo off
set SUBSTANDEPAINTER_PATH="C:\Program Files\Adobe\Adobe Substance 3D Painter\Adobe Substance 3D Painter.exe"
set "SHELF_PATH=%~dp0shelf"

:: add env variable
set OCIO=%~dp0OCIO\simple.config.ocio

set "SOURCE_PATH=%~dp0export-presets"
set "TARGET_PATH=%USERPROFILE%\Documents\Adobe\Adobe Substance 3D Painter\assets\export-presets"

set "SOURCE_SMART_MATERIAL=%~dp0smart-materials"
set "TARGET_SMART_MATERIAL=%USERPROFILE%\Documents\Adobe\Adobe Substance 3D Painter\assets\smart-materials"
xcopy "%SOURCE_PATH%\*" "%TARGET_PATH%\" /E /H /Y
xcopy "%SOURCE_SMART_MATERIAL%\*" "%TARGET_SMART_MATERIAL%\" /E /H /Y

start "" %SUBSTANDEPAINTER_PATH%
exit