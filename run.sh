#!/bin/bash

# Activate the virtual environment
source venv/bin/activate

# Set the FLASK_APP environment variable
export FLASK_APP=main.py

# Start the Flask app in the background with auto-reloading enabled and capture its PID (process ID)
flask run --reload &
FLASK_PID=$!

# Wait for user input to close the app
echo "Flask app is running. Press any key to stop..."
read -n 1

# Kill the Flask process
kill $FLASK_PID

# Wait for a moment to ensure the process is killed
sleep 2

# If the Flask process doesn't shut down gracefully, forcefully kill any processes on port 5000
lsof -t -i:5000 | xargs kill -9 2> /dev/null

# Deactivate the virtual environment
deactivate

echo "Flask app stopped and virtual environment deactivated."
