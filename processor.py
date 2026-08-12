import json
from typing import List, Dict

class GameDataProcessor:
    def __init__(self, data: List[Dict]):
        self.data = data

    def filter_by_genre(self, genre: str) -> List[Dict]:
        filtered_data = [game for game in self.data if game.get('genre') == genre]
        return filtered_data

    def sort_by_rating(self) -> List[Dict]:
        sorted_data = sorted(self.data, key=lambda x: x.get('rating', 0), reverse=True)
        return sorted_data

    def to_json(self) -> str:
        return json.dumps(self.data, indent=4)

# Example usage
if __name__ == '__main__':
    sample_data = [
        {'title': 'Game A', 'genre': 'Action', 'rating': 9.1},
        {'title': 'Game B', 'genre': 'Adventure', 'rating': 8.5},
        {'title': 'Game C', 'genre': 'Action', 'rating': 9.5},
    ]
    processor = GameDataProcessor(sample_data)
    print(processor.filter_by_genre('Action'))  # Filter Action games
    print(processor.sort_by_rating())  # Sort all games by rating
    print(processor.to_json())  # Get JSON representation of data
