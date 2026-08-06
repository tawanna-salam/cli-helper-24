import json
from typing import Any, Dict, List, Union

def load_json(file_path: str) -> Union[Dict[str, Any], List[Any]]:
    """Load JSON data from a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def save_json(data: Union[Dict[str, Any], List[Any]], file_path: str) -> None:
    """Save data to a JSON file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


def pretty_print_json(data: Union[Dict[str, Any], List[Any]]) -> None:
    """Print JSON data in a readable format."""
    print(json.dumps(data, indent=4))


def merge_dicts(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """Merge two dictionaries into one."""
    merged = dict1.copy()  # Create a copy of the first dictionary
    merged.update(dict2)   # Update with the second dictionary
    return merged


def flatten_list_of_dicts(list_of_dicts: List[Dict[str, Any]], key: str) -> List[Any]:
    """Flatten list of dictionaries by a specific key."""
    return [d[key] for d in list_of_dicts if key in d]  # Extract values by key
