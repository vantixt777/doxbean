@echo off
REM Installiere benötigte Python-Module

REM Stelle sicher, dass pip aktualisiert ist
python -m pip install --upgrade pip

REM Installiere Module
pip install requests
pip install PyQt5

REM Hinweis: Die anderen Module (sys, random, threading, datetime) sind Teil der Standardbibliothek
echo.
echo Alle erforderlichen Module wurden installiert.
pause
