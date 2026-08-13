import time
import random

MAX_RETRIES = 5
RETRY_DELAY = 2  # seconds

class NetworkError(Exception):
    pass

class API:
    @staticmethod
    def fetch_data(url):
        # Simulate network operation
        if random.choice([True, False]):  # Randomly succeed or fail
            return {'data': 'some_data'}
        else:
            raise NetworkError('Network request failed')

def retry_network_operation(url):
    retries = 0
    while retries < MAX_RETRIES:
        try:
            return API.fetch_data(url)
        except NetworkError as e:
            retries += 1
            print(f'Retry {retries}/{MAX_RETRIES} failed: {str(e)}')
            time.sleep(RETRY_DELAY)
    raise Exception('Max retries exceeded')
