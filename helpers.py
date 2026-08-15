import random
import logging

# Set up logging
def setup_logging():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

# Function to simulate fetching game data
def fetch_game_data(game_id):
    try:
        if not isinstance(game_id, int) or game_id < 0:
            raise ValueError('Invalid game_id: Must be a non-negative integer.')
        # Simulate a random failure
        if random.random() < 0.2:
            raise ConnectionError('Failed to connect to the game database.')
        # Simulate fetching data
        return {'id': game_id, 'name': f'Game-{game_id}', 'rating': random.uniform(1, 10)}
    except ValueError as ve:
        logging.error(ve)
        return None
    except ConnectionError as ce:
        logging.error(ce)
        return None
    except Exception as e:
        logging.error('An unexpected error occurred: %s', e)
        return None

# Example of usage
if __name__ == '__main__':
    setup_logging()
    game_data = fetch_game_data(1)  # Valid game_id
    if game_data:
        logging.info('Fetched game data: %s', game_data)
    game_data = fetch_game_data(-1)  # Invalid game_id
    game_data = fetch_game_data('abc')  # Invalid game_id
    game_data = fetch_game_data(2)  # Another valid game_id