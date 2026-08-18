import time
import random

class Game:
    def __init__(self, levels):
        self.levels = levels
        self.current_level = 0
        self.score = 0

    def play_level(self):
        level_time = time.time()
        print(f"Playing level {self.current_level + 1}...")
        time.sleep(random.uniform(0.5, 2))  # Simulate game play
        self.score += random.randint(10, 100)
        self.current_level += 1
        print(f"Level {self.current_level} completed. Score: {self.score}")
        return time.time() - level_time

    def play_game(self):
        start_time = time.time()
        for _ in range(self.levels):
            self.play_level()
        print(f"Game finished. Total score: {self.score}")
        print(f"Total time: {time.time() - start_time:.2f} seconds")

if __name__ == '__main__':
    game = Game(levels=5)
    game.play_game()