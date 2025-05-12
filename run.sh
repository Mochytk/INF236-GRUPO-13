#!/bin/sh

x-terminal-emulator -- bash -c "cd app/paes && python3 manage.py runserver; exec bash"

# Start npm in the frontend directory in another new terminal
x-terminal-emulator -- bash -c "cd app/vue && npm start; exec bash"
