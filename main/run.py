from main.gameDisplay import GameDisplay
from main.gameEngine import GameEngine
from main.game_levels import game_level

if __name__ == '__main__':
    GameEngine().run_game(game_level,GameDisplay)