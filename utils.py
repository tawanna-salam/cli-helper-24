import time
import requests


def retry_request(url, max_retries=3, delay=2, backoff=2):
    """Perform a network request with retry logic."
    for attempt in range(max_retries):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Assume we want JSON response
        except requests.exceptions.RequestException as e:
            print(f'Network error: {e}')
            if attempt < max_retries - 1:
                time.sleep(delay)
                delay *= backoff  # Exponential backoff
            else:
                raise


# Example usage: 
# data = retry_request('https://api.example.com/data')
# print(data)