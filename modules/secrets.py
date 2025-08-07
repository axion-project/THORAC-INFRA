import os
from utils.logger import log

def inject(config):
    secrets = config.get("secrets", {})
    for key, val in secrets.items():
        env_var = val.replace("${ENV_", "").replace("}", "")
        value = os.getenv(env_var, "NOT_SET")
        log(f"Injecting secret {key} -> {'***' if value != 'NOT_SET' else 'NOT SET'}")
