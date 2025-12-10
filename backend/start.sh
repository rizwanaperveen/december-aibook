#!/bin/bash

# Start the FastAPI backend server

# Activate virtual environment if it exists
if [ -d ".venv" ]; then
    source .venv/bin/activate
fi

# Install dependencies if requirements.txt exists
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
fi

# Start the FastAPI server
echo "Starting the Embodied AI Systems RAG API server..."
uvicorn main:app --host 0.0.0.0 --port 8000 --reload