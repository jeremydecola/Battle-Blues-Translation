@echo off
type nul > text.txt
for /F "tokens=* delims=|" %%i in ('dir /b /a-d *.*') do if not %%~xi==.bat if not %%~xi==.txt echo %%i >> text.txt