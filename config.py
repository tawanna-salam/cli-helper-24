import json
import os

class ConfigLoader:
    def __init__(self, default_config_path, user_config_path):
        self.default_config_path = default_config_path
        self.user_config_path = user_config_path
        self.config = self.load_config()

    def load_config(self):
        # Load default configuration
        config = self.load_json(self.default_config_path)
        # Load user configuration, if it exists
        user_config = self.load_json(self.user_config_path)
        if user_config:
            config.update(user_config)  # Override defaults with user settings
        return config

    def load_json(self, path):
        try:
            if os.path.exists(path):
                with open(path, 'r') as f:
                    return json.load(f)
            return {}
        except json.JSONDecodeError:
            print(f'Error reading JSON from {path}')
            return {}
        except Exception as e:
            print(f'Unexpected error: {e}')
            return {}

# Example usage:
if __name__ == '__main__':
    loader = ConfigLoader('default_config.json', 'user_config.json')
    print(loader.config)  # Output the loaded configuration