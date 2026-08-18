# Constants for game configurations

# Default screen dimensions
DEFAULT_SCREEN_WIDTH = 1280
DEFAULT_SCREEN_HEIGHT = 720

# FPS settings
DEFAULT_FPS = 60

# Game states
class GameState:
    MENU = 'menu'
    PLAYING = 'playing'
    PAUSED = 'paused'
    GAME_OVER = 'game_over'

# Player settings
DEFAULT_PLAYER_HEALTH = 100
DEFAULT_PLAYER_SPEED = 5

# Enemy settings
DEFAULT_ENEMY_HEALTH = 50
DEFAULT_ENEMY_SPEED = 3

# Difficulty levels
class Difficulty:
    EASY = 'easy'
    NORMAL = 'normal'
    HARD = 'hard'
    INSANE = 'insane'

# Color constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define game version
GAME_VERSION = '1.0.0'