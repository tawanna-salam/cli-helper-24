import json
import os

class ConfigLoader:
    def __init__(self, default_config_file='default_config.json', user_config_file='user_config.json'):
        self.default_config = self.load_config(default_config_file)
        self.user_config = self.load_config(user_config_file)
        self.final_config = self.merge_configs(self.default_config, self.user_config)

    def load_config(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                return json.load(file)
        return {}  # Return empty dict if file does not exist

    def merge_configs(self, default, user):
        combined = default.copy()  # Start with default config
        combined.update(user)  # Update with user config
        return combined

    def get(self, key, default=None):
        return self.final_config.get(key, default)

# Example usage:
# if __name__ == '__main__':
#     config_loader = ConfigLoader()
#     print(config_loader.get('some_option', 'default_value'))