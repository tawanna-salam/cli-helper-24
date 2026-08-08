from typing import List


def process_data(data: List[int]) -> int:
    """
    Processes the list of integers.

    Args:
        data (List[int]): A list of integers to process.

    Returns:
        int: The sum of integers in the list.
    """
    total = sum(data)
    return total


def filter_data(data: List[int], threshold: int) -> List[int]:
    """
    Filters out integers less than the specified threshold.

    Args:
        data (List[int]): A list of integers to filter.
        threshold (int): The threshold value.

    Returns:
        List[int]: A list of integers that are greater than or equal to the threshold.
    """
    return [num for num in data if num >= threshold]


def main() -> None:
    """
    Main function to demonstrate processing and filtering of data.
    """
    sample_data = [1, 2, 3, 4, 5]
    threshold_value = 3
    print(f"Sum: {process_data(sample_data)}")
    print(f"Filtered Data: {filter_data(sample_data, threshold_value)}")


if __name__ == "__main__":
    main()