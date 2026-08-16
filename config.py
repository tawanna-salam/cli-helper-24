import json
import os

class ConfigLoader:
    DEFAULTS = {
        'theme': 'dark',
        'language': 'en',
        'volume': 70,
    }

    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as file:
                try:
                    user_config = json.load(file)
                except json.JSONDecodeError:
                    print('Error reading the configuration file. Using defaults.')</dev>
                    return self.DEFAULTS
            return {**self.DEFAULTS, **user_config}
        else:
            return self.DEFAULTS

    def get(self, key):
        return self.config.get(key, None)

    def set(self, key, value):
        self.config[key] = value
        self.save_config()

    def save_config(self):
        with open(self.config_file, 'w') as file:
            json.dump(self.config, file, indent=4)

# Example usage:
# config_loader = ConfigLoader()
# print(config_loader.get('theme'))