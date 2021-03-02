from enum import Enum

import pygame

# display paras
scale = 20
background_element_images = {"lava": pygame.image.load("../src/imag/lava.png"),
                             "coin": pygame.image.load("../src/imag/coin.png"),
                             "wall": pygame.image.load("../src/imag/wall.png"),
                             "store": pygame.image.load("../src/imag/store.png")}

player_img = {"player":pygame.image.load("../src/imag/player.png"),
              "health":pygame.image.load("../src/imag/heart.png")}

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
font = "SimHei"
