from typing import List, Dict, Any


def process_data(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Process a list of data dictionaries by performing transformations.

    Args:
        data (List[Dict[str, Any]]): A list of dictionaries containing data to process.

    Returns:
        List[Dict[str, Any]]: A list of processed data dictionaries.
    """
    processed_data = []
    for item in data:
        transformed_item = {key: str(value).upper() for key, value in item.items()}
        processed_data.append(transformed_item)
    return processed_data


def aggregate_data(data: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Aggregate data from a list of dictionaries by summing numeric values.

    Args:
        data (List[Dict[str, Any]]): A list of dictionaries to aggregate.

    Returns:
        Dict[str, Any]: A dictionary containing aggregated results.
    """
    aggregation_result = {}
    for item in data:
        for key, value in item.items():
            if isinstance(value, (int, float)):
                aggregation_result[key] = aggregation_result.get(key, 0) + value
    return aggregation_result
