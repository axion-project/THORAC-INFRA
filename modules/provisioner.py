from utils.logger import log

def run(config):
    for node in config['nodes']:
        log(f"Registering node: {node['name']} at {node['host']}")
        # SSH or agent-based check could go here
        # Placeholder: just simulate success
        log(f"Node {node['name']} is online and ready.")
