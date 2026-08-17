import json
import os

class ConfigLoader:
    def __init__(self, default_config_path='default_config.json'):
        self.default_config_path = default_config_path
        self.config = self.load_defaults()

    def load_defaults(self):
        if not os.path.exists(self.default_config_path):
            raise FileNotFoundError(f'Default config file not found: {self.default_config_path}')
        with open(self.default_config_path, 'r') as file:
            return json.load(file)

    def load_custom(self, custom_config_path):
        if os.path.exists(custom_config_path):
            with open(custom_config_path, 'r') as file:
                custom_config = json.load(file)
            return {**self.config, **custom_config}
        return self.config

    def get_config(self, custom_config_path=None):
        if custom_config_path:
            return self.load_custom(custom_config_path)
        return self.config

if __name__ == '__main__':
    loader = ConfigLoader()
    config = loader.get_config('user_config.json')
    print(config)