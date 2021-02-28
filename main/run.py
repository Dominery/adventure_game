import time

import pygame

from main.gameDisplay import GameDisplay
from main.game_levels import game_level
from main.keysContainer import KeysContainer
from main.level import Level
from main.state import State


class EventListener:
    def __init__(self):
        self._event = {}

    def add_event(self, key_type, handler):
        self._event[key_type] = handler

    def remove_event(self, key_type):
        del self._event[key_type]

    def run(self, event):
        for event_type in self._event.keys():
            if event_type == event.type:
                self._event[event_type](event)


def trackKeys(event_listener, keys):
    keys_map = {"ArrowDown": pygame.K_DOWN, "ArrowUp": pygame.K_UP,
                "ArrowLeft": pygame.K_LEFT, "ArrowRight": pygame.K_RIGHT,
                }
    down = KeysContainer(keys)

    def track(event):
        if event.key in map(lambda x: keys_map[x], keys):
            key = filter(lambda x: keys_map[x] == event.key, keys_map.keys())
            down[next(key)] = event.type == pygame.KEYDOWN

    event_listener.add_event(pygame.KEYDOWN, track)
    event_listener.add_event(pygame.KEYUP, track)

    def unregister():
        event_listener.remove_event(pygame.KEYUP)
        event_listener.remove_event(pygame.KEYDOWN)

    down.unregister = unregister
    return down


def run_animation(frame_func):
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


def run_level(level, Display):
    display = Display(screen, level)
    state = State.start(level)
    ending = 0.5
    running = True

    event_listener = EventListener()
    arrow_keys = trackKeys(event_listener, ["ArrowLeft", "ArrowRight", "ArrowUp"])

    def game_exit():
        state.status = "exit"

    event_listener.add_event(pygame.QUIT, lambda x: game_exit())

    def frame(time):
        nonlocal ending, state
        if not running:
            return True
        for event in pygame.event.get():
            event_listener.run(event)
        state = state.update(time, arrow_keys)
        display.sync_state(state)
        if state.status == "playing":
            return True
        elif ending > 0:
            ending -= time
            return True
        else:
            display.clear()
            arrow_keys.unregister()
            return False

    run_animation(frame)
    return state.status


def runGame(plans, Display):
    level = 0
    while level < len(plans):
        status = run_level(Level(plans[level]), Display)
        if status == "won":
            level += 1
        if status == "exit":
            break
    pygame.quit()


def init():
    pygame.init()
    screen = pygame.display.set_mode((640, 420))
    pygame.display.set_caption("adventure")
    return screen


screen = init()
runGame(game_level, GameDisplay)
