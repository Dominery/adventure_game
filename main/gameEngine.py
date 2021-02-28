import time

import pygame

from main.eventHandle import EventListener, trackKeys
from main.level import Level
from main.settings import Status
from main.state import State


class GameEngine:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 420))
        pygame.display.set_caption("adventure")
        self.store_state = None

    def run_game(self,plans,Display):
        level = 0
        while level < len(plans):
            status = self._run_level(Level(plans[level]), Display)
            if status == Status.WON:
                level += 1
            if status == Status.EXIT:
                return pygame.quit()

    def _run_level(self,level,Display):
        display = Display(self.screen, level)
        state = State.start(level)
        ending = 0.5
        running = True

        event_listener = EventListener()
        arrow_keys = trackKeys(event_listener, ["ArrowLeft", "ArrowRight", "ArrowUp"])

        def game_exit():
            state.status = Status.EXIT

        event_listener.add_event(pygame.QUIT, lambda x: game_exit())

        def frame(time):
            nonlocal ending, state
            if not running:
                return True
            for event in pygame.event.get():
                event_listener.run(event)
            state = state.update(time, arrow_keys)
            display.sync_state(state)
            if state.status == Status.PLAYING:
                return True
            elif ending > 0:
                ending -= time
                return True
            else:
                arrow_keys.unregister()
                return False

        self._run_animation(frame)
        return state.status

    def _run_animation(self,frame_func):
        last_time = None
        running = True
        clock = pygame.time.Clock()

        def frame(now):
            nonlocal last_time, running
            if last_time:
                time_step = min(now - last_time, 0.1)
                if not frame_func(time_step):
                    running = False
            last_time = now

        while running:
            clock.tick(60)
            frame(time.time())
