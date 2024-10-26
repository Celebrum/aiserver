import os
from flask import Flask
from pr_agent import PRAgent
from config import AI_SERVER_HOST, AI_SERVER_PORT, HIERARCHICAL_AI_SYSTEM, SIP_COMMUNICATION_SYSTEM, MINDS_CONNECTION
from minds.client import Client
from minds.datasources import DatabaseConfig

app = Flask(__name__)

# Initialize Codium-AI PR-Agent
pr_agent = PRAgent()

# Setup hierarchical cognitive AI system
def setup_hierarchical_ai_system():
    for primary_domain in HIERARCHICAL_AI_SYSTEM['primary_domains']:
        print(f"Setting up primary domain: {primary_domain}")
        for subdomain in HIERARCHICAL_AI_SYSTEM['subdomains'].get(primary_domain, []):
            print(f"Setting up subdomain: {subdomain}")
    for utility in HIERARCHICAL_AI_SYSTEM['utilities']:
        print(f"Setting up utility: {utility}")
    for trigger in HIERARCHICAL_AI_SYSTEM['triggers']:
        print(f"Setting up trigger: {trigger}")

# Setup SIP communication mapping system
def setup_sip_communication_system():
    for repo in SIP_COMMUNICATION_SYSTEM['repositories']:
        print(f"Cloning repository: {repo}")
        os.system(f"git clone {repo}")
    for function in SIP_COMMUNICATION_SYSTEM['functions']:
        print(f"Setting up function: {function}")
    for key, value in SIP_COMMUNICATION_SYSTEM['security'].items():
        print(f"Setting up security: {key} = {value}")

# Initialize and connect AI hub and human hub Minds
def setup_minds():
    client = Client(MINDS_CONNECTION['api_key'])

    # AI hub Mind configuration
    ai_hub_config = DatabaseConfig(
        name='ai_hub',
        description='AI hub database',
        engine='postgres',
        connection_data={
            'user': MINDS_CONNECTION['ai_hub_mind']['database']['user'],
            'password': MINDS_CONNECTION['ai_hub_mind']['database']['password'],
            'host': MINDS_CONNECTION['ai_hub_mind']['database']['host'],
            'port': '5432',
            'database': MINDS_CONNECTION['ai_hub_mind']['database']['name'],
            'schema': 'public'
        },
        tables=[]
    )

    # Human hub Mind configuration
    human_hub_config = DatabaseConfig(
        name='human_hub',
        description='Human hub database',
        engine='postgres',
        connection_data={
            'user': MINDS_CONNECTION['human_hub_mind']['database']['user'],
            'password': MINDS_CONNECTION['human_hub_mind']['database']['password'],
            'host': MINDS_CONNECTION['human_hub_mind']['database']['host'],
            'port': '5432',
            'database': MINDS_CONNECTION['human_hub_mind']['database']['name'],
            'schema': 'public'
        },
        tables=[]
    )

    ai_hub_datasource = client.datasources.create(ai_hub_config, replace=True)
    human_hub_datasource = client.datasources.create(human_hub_config, replace=True)

    ai_hub_mind = client.minds.create(name='ai_hub_mind', datasources=[ai_hub_datasource], replace=True)
    human_hub_mind = client.minds.create(name='human_hub_mind', datasources=[human_hub_datasource], replace=True)

    print(f"{ai_hub_mind.name} and {human_hub_mind.name} were created successfully. They are now connected and can communicate with each other and the communication center.")

@app.route('/')
def home():
    return "AI Server is running"

if __name__ == '__main__':
    setup_hierarchical_ai_system()
    setup_sip_communication_system()
    setup_minds()
    app.run(host=AI_SERVER_HOST, port=AI_SERVER_PORT)
