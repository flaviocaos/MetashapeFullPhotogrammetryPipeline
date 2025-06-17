@echo off
REM === Script para executar o pipeline Metashape via terminal do Windows ===

REM Caminho para o executável do Metashape
set METASHAPE_PATH="C:\Program Files\Agisoft\Metashape Pro\metashape.exe"

REM Caminho para o script Python
set SCRIPT_PATH="C:\caminho\para\metashape_full_pipeline.py"

REM Executar o script
%METASHAPE_PATH% -r %SCRIPT_PATH%

pause
