import os
import json

def read_json(file_path):
    """Reads a JSON file and returns its contents as a dictionary."""
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    if not file_path.endswith('.json'):
        raise ValueError("The provided file path is not a JSON file.")
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        raise ValueError(f"Error decoding JSON from file '{file_path}': {e}")
    except Exception as e:
        raise RuntimeError(f"An error occurred while reading '{file_path}': {e}")


def write_json(file_path, data):
    """Writes a dictionary to a JSON file."""
    if not file_path.endswith('.json'):
        raise ValueError("The provided file path is not a JSON file.")
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        raise RuntimeError(f"An error occurred while writing to '{file_path}': {e}")
