import math
from time import time

import pygame

from main.settings import scale, images, player_x_overlap, player_img, Status


class GameDisplay:
    def __init__(self, screen, level):
        self.screen = screen
        self.level = level
        width = screen.get_width()
        height = screen.get_height()

        self.viewport = {"left": 0, "top": 0, "width": width / scale,
                         "height": height / scale}
        self.background = pygame.Rect(0, 0, width, height)
        self.flip_player = False

    def clear_display(self, status):
        if status == Status.WON:
            self.screen.fill([68, 191, 255], self.background)
        elif status == Status.LOST:
            self.screen.fill([44, 136, 214], self.background)
        else:
            self.screen.fill([52, 166, 251], self.background)

    def sync_state(self, state):
        self.update_viewport(state)
        self.clear_display(state.status)
        self.draw_background(state.level)
        self.draw_actors(state.actors)
        pygame.display.flip()

    def update_viewport(self, state):
        view = self.viewport
        margin = view["width"] / 4
        player = state.player
        center = player.pos.plus(player.size.times(0.5))

        if center.x < view["left"] + margin:
            view["left"] = max(center.x - margin, 0)
        elif center.x > view["left"] + view["width"] - margin:
            view["left"] = min(center.x + margin - view["width"],
                               state.level.width - view["width"])
        if center.y < view["top"] + margin:
            view["top"] = max(center.y - margin, 0)
        elif center.y > view["top"] + view["height"] - margin:
            view["top"] = min(center.y + margin - view["height"],
                              state.level.height - view["height"])

    def draw_background(self, level):
        [left, top, width, height] = self.viewport.values()
        x_start = math.floor(left)
        x_end = math.ceil(left + width)
        y_start = math.floor(top)
        y_end = math.ceil(top + height)

        for y in range(y_start, y_end):
            for x in range(x_start, x_end):
                title = level.rows[y][x]
                if title == "empty":
                    continue
                screen_x = (x - left) * scale
                screen_y = (y - top) * scale
                img = pygame.transform.scale(images[title], (scale, scale))
                self.screen.blit(img, (screen_x, screen_y))

    def draw_actors(self, actors):
        for actor in actors:
            width = int(actor.size.x * scale)
            height = int(actor.size.y * scale)
            x = (actor.pos.x - self.viewport["left"]) * scale
            y = (actor.pos.y - self.viewport["top"]) * scale

            if actor.type == "player":
                self.draw_player(actor, x, y, width, height)
            else:
                img = pygame.transform.scale(images[actor.type], (width, height))
                self.screen.blit(img, (x, y))

    def draw_player(self, player, x, y, width, height):
        width += player_x_overlap * 2
        x -= player_x_overlap
        if player.speed.x != 0:
            self.flip_player = player.speed.x < 0

        tile = 8
        if player.speed.y != 0:
            tile = 9
        elif player.speed.x != 0:
            tile = math.floor(time()*10) % 8

        player_surf = player_img.subsurface(pygame.Rect(width * tile, 0, width, height)).copy()
        if self.flip_player:
            player_surf = pygame.transform.flip(player_surf, True, False)
        self.screen.blit(player_surf, (x, y))
