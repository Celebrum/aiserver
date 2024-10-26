# Project: AI Server for Automated Development Tasks

## Project Description and Purpose

This project aims to create an AI server that automates various development tasks such as creating documents, coding, and managing secrets. The server is equipped with tools like face recognition and emotional awareness to enhance its capabilities. The AI server will be the central server, connected to Ngrok and Nginx for tunneling, and will automate the activation of the appropriate conda environment and docker daemon. The system will use a network of containers with preloaded images to build models and execute tasks. The AI server will be connected to a YouTrack server for user registration and task management.

## Setup Instructions for Codium-AI PR-Agent

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/aiserver.git
   cd aiserver
   ```

2. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the Codium-AI PR-Agent:
   ```bash
   cp .pr_agent.toml.example .pr_agent.toml
   ```

4. Configure the PR-Agent settings in `.pr_agent.toml`:
   ```toml
   [config]
   model="custom_model_name"
   model_turbo="custom_model_name"
   fallback_models=["custom_model_name"]
   custom_model_max_tokens=8000
   ```

5. Start the AI server:
   ```bash
   docker-compose up
   ```

## Usage Instructions for the AI Server

1. Access the AI server through the provided URL.
2. Use the AI server to automate development tasks such as creating documents, coding, and managing secrets.
3. The AI server will handle tasks like reviewing, improving, and updating code.
4. The AI server will continuously gather new data, process it, and update its long-term memory to enable ongoing learning and knowledge expansion.

## Hierarchical Cognitive AI System

The AI server includes a hierarchical cognitive AI system that mimics the human brain's decision-making processes. The system is organized into a hierarchical structure with primary domains, subdomains, utilities, and specific triggers or functions. The AI system integrates with external tools and services like Vercel, Supabase, Datastack, MindDB, and SuperAGI.com. The system continuously gathers new data, processes it, and updates its long-term memory to enable ongoing learning and knowledge expansion. The AI system also incorporates quantum computing capabilities for advanced decision-making and optimization.

## SIP Communication Mapping System

The project includes a free SIP communication mapping system using multiple repositories for phone routing, API calls, and inventory management. The system converts SIP IP calls into SIP API calls with numerical value dependency activation. It includes a central inventory management system to classify and manage user data, including phone numbers, API values, and email addresses. The system ensures data privacy and security by creating encrypted orbs that store user secrets and can only be accessed within a secure environment.

## Setup Instructions for AI Hub and Human Hub Minds

1. Configure the AI hub Mind:
   * Use the database connection details provided for the AI hub:
     * Database Name: `xxdu2672_ai_hub`
     * Database User: `xxdu2672_ai_hub`
     * Database Password: `]3y3p7C@oS`
     * Database Host: `localhost`

2. Configure the human hub Mind:
   * Use the database connection details provided for the human hub:
     * Database Name: `xxdu2672_human_hub`
     * Database User: `xxdu2672_human_hub`
     * Database Password: `)[jp3t5D7S`
     * Database Host: `localhost`

3. Connect the AI hub and human hub Minds:
   * Use the Minds API to link the two Minds, allowing them to share and exchange information.
   * Ensure that both Minds are configured to communicate with each other and the communication center.

## Connecting the Minds to the Communication Center

1. Use the Minds API to link the AI hub and human hub Minds to the communication center.
2. Ensure that the Minds are configured to communicate with the communication center and share information seamlessly.
3. Refer to the Minds API documentation for detailed instructions on how to set up and connect the Minds to the communication center.
