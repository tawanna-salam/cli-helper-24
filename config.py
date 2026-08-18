import json
import os

class ConfigError(Exception):
    pass

class Config:
    def __init__(self, file_path):
        self.file_path = file_path
        self.config_data = {}  
        self.load_config()

    def load_config(self):
        if not os.path.isfile(self.file_path):
            raise ConfigError(f'Config file not found: {self.file_path}')
        try:
            with open(self.file_path, 'r') as config_file:
                self.config_data = json.load(config_file)
        except json.JSONDecodeError:
            raise ConfigError('Error decoding JSON from config file')
        except Exception as e:
            raise ConfigError(f'Unexpected error: {str(e)}')

    def get(self, key, default=None):
        if key not in self.config_data:
            return default
        return self.config_data[key]

    def save(self):
        try:
            with open(self.file_path, 'w') as config_file:
                json.dump(self.config_data, config_file, indent=4)
        except Exception as e:
            raise ConfigError(f'Unable to save config: {str(e)}')

# Example usage
if __name__ == '__main__':
    config = Config('settings.json')
    print(config.get('username', 'Guest'))
    config.config_data['username'] = 'Player1'
    config.save()