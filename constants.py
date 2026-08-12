import time
import random

RETRY_ATTEMPTS = 3
RETRY_DELAY = 2

class NetworkError(Exception):
    pass

class Retry:
    @staticmethod
    def with_retry(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < RETRY_ATTEMPTS:
                try:
                    return func(*args, **kwargs)
                except NetworkError as e:
                    attempts += 1
                    if attempts == RETRY_ATTEMPTS:
                        print(f'Operation failed after {attempts} attempts: {e}')
                        raise
                    delay = RETRY_DELAY + random.uniform(0, 1)
                    print(f'Retrying in {delay:.2f} seconds...')
                    time.sleep(delay)
        return wrapper
