@echo off


REM Activate the virtual environment
venv\Scripts\activate

REM Set the FLASK_APP environment variable
set FLASK_APP=main.py

REM Start the Flask app
start /B flask run

REM Wait for user input to close the app
pause

REM Kill the Flask process
taskkill /F /IM python.exe

REM Deactivate the virtual environment
call deactivate.bat

echo Flask app stopped and virtual environment deactivated.
