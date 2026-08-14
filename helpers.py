import random
from typing import List

class GameError(Exception):
    pass

class NoPlayersError(GameError):
    pass

class Game:
    def __init__(self, players: List[str]):
        if not players:
            raise NoPlayersError("At least one player is required.")
        self.players = players
        self.current_player = 0

    def next_turn(self):
        if not self.players:
            raise NoPlayersError("Cannot proceed, no players to take turns.")
        player = self.players[self.current_player]
        print(f"It's {player}'s turn!")
        self.current_player = (self.current_player + 1) % len(self.players)

    def roll_dice(self):
        try:
            return random.randint(1, 6)
        except Exception as e:
            raise GameError(f"Error rolling dice: {e}")

if __name__ == '__main__':
    try:
        game = Game(["Alice", "Bob"])
        for _ in range(5):
            game.next_turn()
            print(f"Rolled: {game.roll_dice()}")
    except GameError as e:
        print(f"Game error occurred: {e}")
    except NoPlayersError as e:
        print(f"Error: {e}")
