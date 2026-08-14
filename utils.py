import json
from typing import Any, Dict

def save_game_data(file_path: str, game_data: Dict[str, Any]) -> None:
    """
    Saves game data to a specified JSON file.
    
    :param file_path: The path to the JSON file where game data will be saved.
    :param game_data: A dictionary containing game data to save.
    """
    with open(file_path, 'w') as file:
        json.dump(game_data, file, indent=4)


def load_game_data(file_path: str) -> Dict[str, Any]:
    """
    Loads game data from a specified JSON file.
    
    :param file_path: The path to the JSON file to load.
    :return: A dictionary containing the loaded game data.
    """
    with open(file_path, 'r') as file:
        return json.load(file)


def update_game_data(file_path: str, updates: Dict[str, Any]) -> None:
    """
    Updates existing game data with new information.
    
    :param file_path: The path to the JSON file containing existing game data.
    :param updates: A dictionary with updates to apply to the game data.
    """
    game_data = load_game_data(file_path)
    game_data.update(updates)
    save_game_data(file_path, game_data)