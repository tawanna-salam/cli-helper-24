import json
from pathlib import Path

DEFAULT_CONFIG = {
    'fullscreen': False,
    'volume': 50,
    'resolution': '1920x1080',
    'controls': {
        'jump': 'space',
        'move_left': 'a',
        'move_right': 'd'
    }
}

class ConfigLoader:
    def __init__(self, config_file: str):
        self.config_file = Path(config_file)
        self.config = self.load_config()

    def load_config(self) -> dict:
        if self.config_file.is_file():
            with open(self.config_file, 'r') as file:
                return self.merge_defaults(json.load(file))
        else:
            return DEFAULT_CONFIG

    def merge_defaults(self, user_config: dict) -> dict:
        combined_config = DEFAULT_CONFIG.copy()
        combined_config.update(user_config)
        return combined_config

    def get(self, key: str, default=None):
        return self.config.get(key, default)

    def set(self, key: str, value):
        self.config[key] = value
        with open(self.config_file, 'w') as file:
            json.dump(self.config, file, indent=4)
