import math

import pygame

scale = 20
images = {"lava": pygame.image.load("../src/lava.png"),
          "coin": pygame.image.load("../src/coin.png"),
          "wall": pygame.image.load("../src/wall.png")}


class GameDisplay:
    def __init__(self, screen, level):
        self.screen = screen
        self.level = level
        self.width = screen.get_width()
        self.height = screen.get_height()

        self.viewport = {"left": 0, "top": 0, "width": self.width / scale,
                         "height": self.height / scale}

    def clear(self):
        background = pygame.Rect(0,0,self.width,self.height)
        self.screen.fill([0,0,0],background)

    def sync_state(self, state):
        self.update_viewport(state)
        self.clear()
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

    def draw_player(self, actor, x, y, width, height):
        rect = pygame.Rect(x,y,width,height)
        self.screen.fill([255,255,255],rect)
