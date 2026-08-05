import json
import os

DEFAULT_CONFIG = {
    'app_name': 'CLI Helper',
    'version': '1.0',
    'max_retries': 5,
    'timeout': 30,
    'log_level': 'INFO'
}

class ConfigLoader:
    def __init__(self, config_file=None):
        self.config_file = config_file
        self.config = DEFAULT_CONFIG.copy()
        if self.config_file:
            self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                user_config = json.load(f)
                self.config.update(user_config)
        else:
            raise FileNotFoundError(f"Config file {self.config_file} not found.")

    def get(self, key, default=None):
        return self.config.get(key, default)

    def __str__(self):
        return json.dumps(self.config, indent=4)