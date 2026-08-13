from typing import List, Tuple


def calculate_score(player_moves: List[Tuple[int, int]]) -> int:
    """
    Calculate the total score based on player moves.

    Each move is a tuple of (x, y) coordinates, and the score is determined
    by the distance from the origin (0, 0).

    Args:
        player_moves (List[Tuple[int, int]]): A list of moves as tuples of coordinates.

    Returns:
        int: The total score calculated from all moves.
    """
    total_score = 0
    for x, y in player_moves:
        distance = (x ** 2 + y ** 2) ** 0.5
        total_score += int(distance)
    return total_score


def determine_winner(scores: List[int]) -> int:
    """
    Determine the index of the player with the highest score.

    Args:
        scores (List[int]): A list of scores for each player.

    Returns:
        int: The index of the winning player.
    """
    return scores.index(max(scores))


if __name__ == '__main__':
    moves = [(1, 2), (3, 4), (5, 6)]
    score = calculate_score(moves)
    print(f"Total score: {score}")
    winner = determine_winner([10, 20, 15])
    print(f"Winner index: {winner}")