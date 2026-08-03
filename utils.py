from typing import List, Optional


def clean_string(input_string: str) -> str:
    """
    Cleans the input string by stripping whitespace
    and converting it to lowercase.
    
    Args:
        input_string (str): The string to be cleaned.
    
    Returns:
        str: The cleaned string.
    """
    return input_string.strip().lower()


def filter_numbers(numbers: List[Optional[int]], threshold: int) -> List[int]:
    """
    Filters out invalid numbers and retains those that
    are greater than the specified threshold.
    
    Args:
        numbers (List[Optional[int]]): A list of integers, may contain None.
        threshold (int): The threshold to filter numbers.
    
    Returns:
        List[int]: A list of integers greater than the threshold.
    """
    return [num for num in numbers if num is not None and num > threshold]


def format_list(items: List[str]) -> str:
    """
    Formats a list of strings into a single comma-separated
    string with an 'and' before the last item.
    
    Args:
        items (List[str]): The list of strings to format.
    
    Returns:
        str: The formatted string.
    """
    if not items:
        return ''
    if len(items) == 1:
        return items[0]
    return ', '.join(items[:-1]) + ' and ' + items[-1]
