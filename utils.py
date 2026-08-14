from typing import List, Dict, Any


def calculate_score(player_stats: Dict[str, int]) -> int:
    """
    Calculate the total score for a player based on their statistics.

    Args:
        player_stats (Dict[str, int]): A dictionary containing player stats such as 'kills', 'deaths', and 'assists'.

    Returns:
        int: The total score calculated by the formula: kills * 10 - deaths * 5 + assists * 2.
    """
    score = player_stats.get('kills', 0) * 10
    score -= player_stats.get('deaths', 0) * 5
    score += player_stats.get('assists', 0) * 2
    return score


def display_leaderboard(players: List[Dict[str, Any]]) -> None:
    """
    Display the leaderboard for players sorted by their scores in descending order.

    Args:
        players (List[Dict[str, Any]]): A list of player dictionaries containing 'name' and 'stats'.
    """
    leaderboard = sorted(players, key=lambda p: calculate_score(p['stats']), reverse=True)
    for rank, player in enumerate(leaderboard, start=1):
        print(f"{rank}. {player['name']} - Score: {calculate_score(player['stats'])}")


def validate_player_data(player_data: Dict[str, Any]) -> bool:
    """
    Validate the player's data to ensure it contains the necessary fields.

    Args:
        player_data (Dict[str, Any]): A dictionary containing player information.

    Returns:
        bool: True if validation passes, False otherwise.
    """
    required_fields = {'name', 'stats'}
    return required_fields.issubset(player_data.keys())
