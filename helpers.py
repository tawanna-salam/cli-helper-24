import os
import json
from typing import Any, Dict


def read_json_file(file_path: str) -> Dict[str, Any]:
    """Read a JSON file and return its content as a dictionary."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} not found")
    with open(file_path, 'r') as file:
        return json.load(file)


def write_json_file(file_path: str, data: Dict[str, Any]) -> None:
    """Write a dictionary to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def list_files_in_directory(directory_path: str) -> None:
    """List all files in a directory."""
    try:
        files = os.listdir(directory_path)
        for file in files:
            print(file)
    except Exception as e:
        print(f"Error reading directory: {e}")