from main.settings import Status


class GameState:
    store_state = None
    player_life = 3

    def __init__(self, level, actors, status):
        self.level = level
        self.actors = actors
        self.status = status

    @classmethod
    def store(cls,state):
        cls.store_state = state

    @classmethod
    def start(cls, level):
        return cls(level, level.start_actors, Status.PLAYING)

    @property
    def player(self):
        player_gen = filter(lambda x: x.type == "player", self.actors)
        return next(player_gen)

    @classmethod
    def decrease_player_life(cls):
        cls.player_life -= 1

    @classmethod
    def reset_player_life(cls):
        cls.player_life = 3

    def update(self, time, keys):
        actors = list(map(lambda actor: actor.update(time, self, keys), self.actors))
        new_state = GameState(self.level, actors, self.status)

        if self.player_life <= 0:
            return GameState(self.level, actors, Status.LOST)

        if new_state.status != Status.PLAYING:
            return new_state

        player = new_state.player
        if self.level.touches(player.pos, player.size, "lava"):
            self.decrease_player_life()
            return GameState(self.level, actors, Status.LIFE_DECREASE)

        if self.level.touches(player.pos, player.size, "store"):
            self.store(self)

        for actor in actors:
            if actor != player and overlap(actor, player):
                new_state = actor.collide(new_state)
        return new_state


def overlap(actor1, actor2):
    return actor1.pos.x + actor1.size.x > actor2.pos.x and \
           actor1.pos.x < actor2.pos.x + actor2.size.x and \
           actor1.pos.y + actor1.size.y > actor2.pos.y and \
           actor1.pos.y < actor2.pos.y + actor2.size.y
