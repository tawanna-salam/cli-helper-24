import random

class GameError(Exception):
    pass

class Game:
    def __init__(self, max_score=100):
        self.max_score = max_score
        self.current_score = 0

    def play_round(self):
        try:
            score = random.randint(1, 20)
            self.current_score += score
            self.check_score()
        except Exception as e:
            raise GameError(f"An error occurred during gameplay: {e}")

    def check_score(self):
        if self.current_score < 0:
            raise GameError("Score cannot be negative.")
        elif self.current_score > self.max_score:
            self.current_score = self.max_score
            print("Max score reached. Resetting to max.")

    def get_score(self):
        return self.current_score

    def reset_game(self):
        self.current_score = 0

# Example usage
if __name__ == '__main__':
    game = Game()
    for _ in range(10):
        game.play_round()
        print(f"Current Score: {game.get_score()}")
        
    game.reset_game()  # Reset game after rounds
    print(f"Score after reset: {game.get_score()}")