import pygame


from main.keysContainer import KeysContainer


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
