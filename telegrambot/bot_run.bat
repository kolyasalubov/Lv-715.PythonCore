@echo off

call %~dp0telegrambot\venv\Scripts\activate

cd %~dp0telegrambot

set TOKEN=5671913537:AAHuF6m1k2M2MAH7A2nBC4OVu7JL2CV9poY

python bot_telegram.py

pause