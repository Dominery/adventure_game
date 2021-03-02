import time

import pygame

from main.eventHandle import EventListener, trackKeys
from main.level import Level
from main.settings import Status
from main.state import State


class GameEngine:
    def __init__(self, screen):
        self.screen = screen

    def run_game(self, plans, Display, level_num=0):
        State.reset_player_life()
        while level_num < len(plans):
            level = Level(plans[level_num])
            status = self._run_level(State.start(level), Display(self.screen, level))
            if status == Status.WON:
                level_num += 1
            if status == Status.EXIT or status == Status.LOST:
                break
        return State.store_state

    def _run_level(self, state, display):
        State.store(state)
        ending = 0.5
        running = True

        event_listener = EventListener()
        arrow_keys = trackKeys(event_listener, ["ArrowLeft", "ArrowRight", "ArrowUp"])

        def game_exit(*args):
            state.status = Status.EXIT

        event_listener.add_event(pygame.QUIT, game_exit)

        def frame(time_spec):
            nonlocal ending, state
            if not running:
                return True
            for event in pygame.event.get():
                event_listener.run(event)
            state = state.update(time_spec, arrow_keys)
            display.sync_state(state)
            if state.status == Status.PLAYING:
                return True
            elif state.status == Status.EXIT or state.status == Status.LOST:
                return False
            elif state.status == Status.LIFE_DECREASE:
                if ending > 0:
                    ending -= time_spec
                else:
                    ending = 0.5
                    state = State.store_state
                return True
            else:
                arrow_keys.unregister()
                return False

        self._run_animation(frame)
        return state.status

    def _run_animation(self, frame_func):
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
