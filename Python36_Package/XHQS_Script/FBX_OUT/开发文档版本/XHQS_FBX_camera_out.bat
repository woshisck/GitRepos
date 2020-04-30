@echo off
 
set PYTHONPATH=H:\TD_HW\XHQS_Script\FBX_OUT
 
set PATH=%PATH%;%PYTHONPATH%

set CURPATH = %cd%
 
for /r  %cd%  %%i in (*.mb) do "C:\Program Files\Autodesk\Maya2018\bin\mayabatch.exe" -file %%i  -command "python(\"import XHQS_FBX_camera_out\")"
pause
