import json
import os

class ConfigLoader:
    def __init__(self, default_config: dict):
        # Initialize with default configuration
        self.default_config = default_config
        self.loaded_config = {}

    def load_config(self, filepath: str) -> dict:
        # Load configuration from a specified file path
        if os.path.exists(filepath):
            with open(filepath, 'r') as config_file:
                self.loaded_config = json.load(config_file)
        else:
            print(f'Config file not found. Using defaults.')
        return {**self.default_config, **self.loaded_config}

if __name__ == '__main__':
    # Example usage of ConfigLoader
    default_settings = {
        'volume': 70,
        'resolution': '1920x1080',
        'fullscreen': True
    }
    config_loader = ConfigLoader(default_settings)
    config = config_loader.load_config('config.json')
    print(config)