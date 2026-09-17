@echo off
title Re4J LCE Modder and Verification Suite
echo ===================================================
echo   Re4J LCE Mod Loader - Automated Setup & Test
echo ===================================================
echo.

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Python is not installed or not added to PATH!
    echo Please install Python 3.x and check 'Add Python to PATH'.
    pause
    exit /b
)

:: Run the script
python test_and_build.py

echo.
echo ===================================================
echo Setup Complete!
echo You can place .py mods into the /mods folder.
echo ===================================================
pause