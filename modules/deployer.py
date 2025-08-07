import subprocess
from utils.logger import log

def deploy_all(config):
    for node in config['nodes']:
        for service in node['services']:
            log(f"Deploying {service} on {node['name']}")
            # Simulated Docker Compose deploy
            subprocess.run(["echo", f"Deploy {service} on {node['host']}"])
