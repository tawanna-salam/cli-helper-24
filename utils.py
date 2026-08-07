from typing import List, Dict, Any


def filter_even_numbers(numbers: List[int]) -> List[int]:
    """
    Filters the even numbers from a given list.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list containing only even integers.
    """
    return [number for number in numbers if number % 2 == 0]


def merge_dictionaries(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """
    Merges two dictionaries into one, with dict2 values overwriting dict1 values if keys overlap.

    Args:
        dict1 (Dict[str, Any]): The first dictionary.
        dict2 (Dict[str, Any]): The second dictionary.

    Returns:
        Dict[str, Any]: A new merged dictionary.
    """
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict


def calculate_average(values: List[float]) -> float:
    """
    Calculates the average of a list of numbers.

    Args:
        values (List[float]): A list of float numbers.

    Returns:
        float: The average of the numbers.
    """
    if not values:
        return 0.0
    return sum(values) / len(values)  
