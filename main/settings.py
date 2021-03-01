from enum import Enum

import pygame

# display paras
scale = 20
images = {"lava": pygame.image.load("../src/imag/lava.png"),
          "coin": pygame.image.load("../src/imag/coin.png"),
          "wall": pygame.image.load("../src/imag/wall.png"),
          "store": pygame.image.load("../src/imag/store.png")}

player_img = pygame.image.load("../src/imag/player.png")

player_x_overlap = 4

# game running
background_music = "../src/music/CastleIntheSky.wav"


class Status(Enum):
    PLAYING = "playing"
    EXIT = "exit"
    LOST = "lost"
    WON = "won"
    LIFE_DECREASE = "life_decrease"


# user interface
background = pygame.image.load("../src/imag/background.jpg")
young_player = pygame.image.load("../src/imag/young_player.png")
icon = pygame.image.load("../src/imag/icon.png")
