import time
import random

class GameLogic:
    def __init__(self, max_score):
        self.max_score = max_score
        self.player_scores = {}

    def add_player(self, player_name):
        self.player_scores[player_name] = 0

    def simulate_round(self, player_name):
        # Simulates a game round and updates the player's score
        score = random.randint(1, 10)
        self.player_scores[player_name] += score
        return score

    def check_winner(self):
        # Returns the first player to reach the max_score
        for player, score in self.player_scores.items():
            if score >= self.max_score:
                return player
        return None

    def play_game(self):
        while True:
            for player in self.player_scores:
                score = self.simulate_round(player)
                print(f'{player} scored {score}, total: {self.player_scores[player]}')
                winner = self.check_winner()
                if winner:
                    print(f'{winner} wins the game!')
                    return
            time.sleep(1)  # Add delay to slow down rounds