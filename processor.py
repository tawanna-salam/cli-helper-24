from typing import List, Dict


def process_data(data: List[Dict[str, int]]) -> List[int]:
    """
    Process a list of dictionaries and return a list of summed values.

    Each dictionary in the input list should have string keys and integer values.
    This function sums the values of each dictionary and returns the result in a list.

    Parameters:
    data (List[Dict[str, int]]): A list of dictionaries to process.

    Returns:
    List[int]: A list of summed integer values from the dictionaries.
    """
    results = []
    for entry in data:
        total = sum(entry.values())
        results.append(total)
    return results

def main() -> None:
    """
    Main function to demonstrate data processing.
    """
    sample_data = [
        {'a': 1, 'b': 2, 'c': 3},
        {'x': 4, 'y': 5},
        {'foo': 10, 'bar': 20, 'baz': 30},
    ]
    processed = process_data(sample_data)
    print(processed)

if __name__ == '__main__':
    main()