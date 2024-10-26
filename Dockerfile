# Dockerfile for AI Server

# Base image
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Install necessary tools and libraries
RUN apt-get update && apt-get install -y \
    nginx \
    ngrok \
    && rm -rf /var/lib/apt/lists/*

# Setup Codium-AI PR-Agent
RUN git clone https://github.com/Celebrum/pr-agent.git /app/pr-agent
WORKDIR /app/pr-agent
RUN pip install --no-cache-dir -r requirements.txt

# Set entrypoint for starting the AI server
ENTRYPOINT ["python", "main.py"]
