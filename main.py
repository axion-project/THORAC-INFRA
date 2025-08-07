from modules import provisioner, deployer, secrets
from utils.logger import log
import yaml

def load_config():
    with open("config/infra_config.yaml", "r") as file:
        return yaml.safe_load(file)

def main():
    config = load_config()
    log("Starting THORAC-INFA...")

    log("Provisioning nodes...")
    provisioner.run(config)

    log("Injecting secrets...")
    secrets.inject(config)

    log("Deploying services...")
    deployer.deploy_all(config)

    log("THORAC-INFA completed successfully.")

if __name__ == "__main__":
    main()
