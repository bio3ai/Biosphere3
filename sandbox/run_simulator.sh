#!/bin/bash

set -e  # Exit immediately if a command exits with a non-zero status

# Define ports
GAME_SERVER_PORT=5003
AGENT_SERVER_PORT=5006

# Start Game and Agent servers
echo "Starting game_http_server.py..."
python sandbox/game_http_server.py &  
GAME_PID=$!

echo "Starting agent_http_server.py..."
python sandbox/agent_http_server.py &  
AGENT_PID=$!

# Function: Wait for a port to be available
wait_for_port() {
    local port=$1
    while ! nc -z localhost $port; do
        sleep 1
    done
    echo "Port $port is now active!"
}

# Wait until both servers are fully started
wait_for_port $GAME_SERVER_PORT
wait_for_port $AGENT_SERVER_PORT

# Start the game simulator
echo "Starting game_simulator.py..."
python sandbox/game_simulator.py &  
SIMULATOR_PID=$!

# Handle SIGINT (Ctrl+C) and ensure all processes are terminated
trap "echo 'Stopping all servers...'; kill $GAME_PID $AGENT_PID $SIMULATOR_PID; exit 1" SIGINT

# Keep the script running and wait for all subprocesses
wait