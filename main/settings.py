from enum import Enum

import pygame

scale = 20
images = {"lava": pygame.image.load("../src/imag/lava.png"),
          "coin": pygame.image.load("../src/imag/coin.png"),
          "wall": pygame.image.load("../src/imag/wall.png")}

player_img = pygame.image.load("../src/imag/player.png")
player_x_overlap = 4
background_music = "../src/music/CastleintheSky.wav"


class Status(Enum):
    PLAYING = "playing"
    EXIT = "exit"
    LOST = "lost"
    WON = "won"
    LIFE_DECREASE = "life_decrease"
