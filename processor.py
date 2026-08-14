import random
import time

class GameProcessor:
    def __init__(self):
        self.score = 0
        self.level = 1
        self.is_running = True
        self.max_level = 10

    def play(self):
        while self.is_running:
            self.process_level()
            self.level += 1
            if self.level > self.max_level:
                self.end_game()

    def process_level(self):
        print(f'--- Level {self.level} ---')
        time.sleep(1)  # Simulating level processing time
        outcome = self.random_outcome()
        if outcome:
            self.score += 10
            print('You scored!')
        else:
            print('Try again!')

    def random_outcome(self):
        return random.choice([True, False])

    def end_game(self):
        self.is_running = False
        print(f'Game Over! Your score: {self.score}')

if __name__ == '__main__':
    game = GameProcessor()
    game.play()