import os
from enum import Enum

import pygame

# display paras
BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"src")
scale = 20

background_element_images = {"lava": pygame.image.load(os.path.join(BASE_DIR,"imag","lava.png")),
                             "coin": pygame.image.load(os.path.join(BASE_DIR,"imag","coin.png")),
                             "wall": pygame.image.load(os.path.join(BASE_DIR,"imag","wall.png")),
                             "store": pygame.image.load(os.path.join(BASE_DIR,"imag","store.png"))}

player_img = {"player": pygame.image.load(os.path.join(BASE_DIR,"imag","player.png")),
              "health": pygame.image.load(os.path.join(BASE_DIR,"imag","heart.png"))}

player_x_overlap = 4

# game running
background_music = os.path.join(BASE_DIR,"music","CastleIntheSky.wav")


class Status(Enum):
    PLAYING = "playing"
    EXIT = "exit"
    LOST = "lost"
    WON = "won"
    LIFE_DECREASE = "life_decrease"


# user interface
background = pygame.image.load(os.path.join(BASE_DIR,"imag","background.jpg"))
young_player = pygame.image.load(os.path.join(BASE_DIR,"imag","young_player.png"))
icon = pygame.image.load(os.path.join(BASE_DIR,"imag","icon.png"))
font = "SimHei"
