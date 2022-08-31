@echo off
pyuic6 main.ui -o main_ui.py
SETLOCAL=ENABLEDELAYEDEXPANSION

fart main_ui.py PyQt6 PySide6
pause