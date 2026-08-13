import json
import os

def load_config(config_file='config.json', defaults=None):
    """Load configuration from a JSON file with defaults."""
    if defaults is None:
        defaults = {}
    
    if not os.path.isfile(config_file):
        return defaults
    
    with open(config_file, 'r') as file:
        try:
            config = json.load(file)
        except json.JSONDecodeError:
            return defaults
        
    return {**defaults, **config}

if __name__ == '__main__':
    default_settings = {'resolution': '1920x1080', 'volume': 75}
    settings = load_config('game_config.json', default_settings)
    print(settings)