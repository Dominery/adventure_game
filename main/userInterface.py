import pygame

from main.button import Button
from main.eventHandle import EventListener
from main.gameDisplay import GameDisplay
from main.gameEngine import GameEngine
from main.game_levels import game_level
from main.settings import background_music, background, young_player, icon


class UserInterface:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 420))
        pygame.display.set_caption("Adventure Game")
        pygame.display.set_icon(icon)
        pygame.mixer.music.load(background_music)
        pygame.mixer.music.set_volume(0.2)
        # pygame.mixer.music.play(-1)
        messages = ['Start']
        self.buttons = [Button(45, (255, 255, 255), (0, 0, 255), i) for i in messages]
        height_length = self.screen.get_height() / 2 / len(messages)
        self.buttons_draw_func = [
            self.buttons[i].set_up((self.screen.get_width() / 2,self.screen.get_height() / 2 + height_length * i ),
                                   self.screen) for i in range(len(self.buttons))]

    def _draw_background(self):
        background_img = pygame.transform.scale(background, self.screen.get_size())
        mask = pygame.Surface(self.screen.get_size()).convert_alpha()
        mask.fill([0, 0, 0])
        mask.set_alpha(70)
        limit_width = int(min(self.screen.get_size()) / 3)
        young_player_img = pygame.transform.scale(young_player,
                                                  min(young_player.get_size(), (limit_width, limit_width)))
        background_img.blit(mask, (0, 0))
        background_img.blit(young_player_img, ((self.screen.get_width() - young_player_img.get_width()) / 2,
                                               0))
        self.screen.blit(background_img, (0, 0))

    def _draw_button(self):
        for func in self.buttons_draw_func:
            func()

    def draw(self):
        self._draw_background()
        self._draw_button()

    def run(self):
        event_listener = EventListener()

        def button_touch_handler(*args):
            for button in self.buttons:
                button.change_color()

        def button_down_handler(event):
            if event.button != 1:
                return
            button = filter(lambda x: x.touch(), self.buttons)
            if button and next(button).msg == "Start":
                pygame.mixer.music.play(-1)
                return GameEngine(self.screen).run_game(game_level, GameDisplay)

        event_listener.add_event(pygame.MOUSEMOTION, button_touch_handler)
        event_listener.add_event(pygame.MOUSEBUTTONDOWN, button_down_handler)

        while True:
            pygame.time.Clock().tick(30)
            for event in pygame.event.get():
                event_listener.run(event)
            self.draw()
            pygame.display.flip()


UserInterface().run()
