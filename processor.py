import time

class GameProcessor:
    def __init__(self):
        self.current_state = 'idle'
        self.last_update_time = time.time()

    def update_state(self, new_state):
        current_time = time.time()
        if current_time - self.last_update_time >= 1:  # Update every 1 second
            self.current_state = new_state
            self.last_update_time = current_time
            print(f'Game state updated to: {self.current_state}')
        else:
            print('State update skipped to optimize performance.')

    def process_input(self, input_action):
        if self.current_state == 'playing':
            self.perform_action(input_action)
        else:
            print('Input ignored, not in a playable state.')

    def perform_action(self, action):
        print(f'Performing action: {action}')

if __name__ == '__main__':
    processor = GameProcessor()
    processor.update_state('playing')
    time.sleep(2)
    processor.process_input('move_forward')
    processor.update_state('paused')
    processor.process_input('move_backward')
