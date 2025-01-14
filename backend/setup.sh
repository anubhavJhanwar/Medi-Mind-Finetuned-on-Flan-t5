#!/bin/bash
# MediMind AI — Backend Setup Script

echo "Setting up MediMind AI backend..."

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Copy env file
if [ ! -f .env ]; then
    cp ../.env.example .env
    echo "Created .env from .env.example — please update values."
fi

echo "Setup complete. Run: python run.py"
