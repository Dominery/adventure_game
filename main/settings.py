from enum import Enum

import pygame

scale = 20
images = {"lava": pygame.image.load("../src/lava.png"),
          "coin": pygame.image.load("../src/coin.png"),
          "wall": pygame.image.load("../src/wall.png")}

player_img = pygame.image.load("../src/player.png")
player_x_overlap = 4


class Status(Enum):
    PLAYING = "playing"
    EXIT = "exit"
    LOST = "lost"
    WON = "won"
    LIFE_DECREASE = "life_decrease"
