import time
import requests
from requests.exceptions import RequestException


def retry_request(url, max_retries=3, backoff_factor=1):
    """
    Perform a GET request with retry logic.
    
    Args:
        url (str): The URL to request.
        max_retries (int): Maximum number of retries before failing.
        backoff_factor (float): Backoff factor for sleep time between retries.
    
    Returns:
        Response: The response object from the GET request if successful.
    """
    for attempt in range(max_retries):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for HTTP errors
            return response
        except RequestException as e:
            if attempt < max_retries - 1:
                sleep_time = backoff_factor * (2 ** attempt)
                print(f'Retry {attempt + 1}/{max_retries} failed: {e}; retrying in {sleep_time} seconds...')
                time.sleep(sleep_time)
            else:
                print('Max retries reached; request failed.')
                raise
