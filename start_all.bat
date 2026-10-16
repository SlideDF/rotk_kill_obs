@echo off
setlocal
cd /d "%~dp0"

echo ==========================================
echo        ROTK KILL COUNTER - LANCEMENT
echo ==========================================
echo.
echo 1/2 - Demarrage du compteur...
start "ROTK Kill Counter - Serveur" cmd /k "cd /d ""%~dp0"" && py server.py"

echo Attente du demarrage du serveur...
timeout /t 2 /nobreak >nul

echo 2/2 - Demarrage des raccourcis clavier...
if exist "%ProgramFiles%\AutoHotkey\v2\AutoHotkey.exe" (
    start "" "%ProgramFiles%\AutoHotkey\v2\AutoHotkey.exe" "%~dp0Hotkey.ahk"
) else if exist "%ProgramFiles%\AutoHotkey\AutoHotkey.exe" (
    start "" "%ProgramFiles%\AutoHotkey\AutoHotkey.exe" "%~dp0Hotkey.ahk"
) else (
    start "" "%~dp0Hotkey.ahk"
)

echo.
echo Le compteur et les raccourcis ont ete lances.
echo Saisissez l'objectif dans la fenetre du serveur si ce n'est pas deja fait.
echo Laissez la fenetre du serveur ouverte pendant le stream.
echo Vous pouvez fermer cette fenetre.
exit /b 0
