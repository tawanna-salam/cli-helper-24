import os
import json
from typing import Any, Dict

def read_json_file(filepath: str) -> Dict[str, Any]:
    """Reads a JSON file and returns its content as a dictionary."""
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)


def write_json_file(filepath: str, data: Dict[str, Any]) -> None:
    """Writes a dictionary to a JSON file."""
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def merge_dicts(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """Merges two dictionaries into one."""
    merged = dict1.copy()
    merged.update(dict2)
    return merged


def clear_temp_files(directory: str) -> None:
    """Deletes all files in the given directory."""
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

