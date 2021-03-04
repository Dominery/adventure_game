import pygame

from main.settings import font


class Button:
    def __init__(self, font_size, font_color, back_color, msg):
        self._font = pygame.font.SysFont(font, font_size)
        self.reversed = False
        self.back_color = back_color
        self.color = font_color
        self.msg = msg
        self.background = pygame.Surface((160, 40))
        self.rect = self.background.get_rect()

    def set_up(self, location, par_surf):
        self.rect.center = location

        def draw():
            msg_img = self._font.render(self.msg, True, self.color)
            self.background.fill(self.back_color)
            rect = msg_img.get_rect()
            rect.center = self.background.get_rect().center
            self.background.blit(msg_img, rect)
            par_surf.blit(self.background, self.rect)
            return rect

        draw()
        return draw

    def change_color(self):
        if not self.touch():
            if self.reversed:
                self.reverse_color()
            self.reversed = False
            return
        if not self.reversed:
            self.reverse_color()
            self.reversed = True

    def reverse_color(self):
        self.color,self.back_color = self.back_color,self.color

    def touch(self):
        if self.rect.collidepoint(*pygame.mouse.get_pos()):
            return True
        return False
