import pygame

from main.settings import background_music, background, young_player, icon


class UserInterface:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640,420))
        pygame.display.set_caption("Adventure Game")
        pygame.display.set_icon(icon)
        pygame.mixer.music.load(background_music)
        pygame.mixer.music.set_volume(0.2)
        # pygame.mixer.music.play(-1)

    def _draw_background(self):
        background_img = pygame.transform.scale(background,self.screen.get_size())
        mask = pygame.Surface(self.screen.get_size()).convert_alpha()
        mask.fill([0,0,0])
        mask.set_alpha(70)
        limit_width = int(min(self.screen.get_size())/3)
        young_player_img = pygame.transform.scale(young_player,min(young_player.get_size(),(limit_width,limit_width)))
        background_img.blit(mask,(0,0))
        background_img.blit(young_player_img,((self.screen.get_width()-young_player_img.get_width())/2,
                                              0))
        self.screen.blit(background_img,(0,0))

    def _draw_button(self):
        pass

    def run(self):
        while True:
            self._draw_background()
            pygame.display.flip()

UserInterface().run()

