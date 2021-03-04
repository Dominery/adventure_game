from main.settings import Status
from main.model.gamestate import GameState
from main.model.vec import Vec


class Lava:
    size = Vec(1,1)

    def __init__(self, pos, speed, reset=None):
        self.pos = pos
        self.speed = speed
        self.reset = reset

    @classmethod
    def create(cls, pos, char=None):
        if char == "=":
            return cls(pos, Vec(2, 0))
        elif char == "|":
            return cls(pos, Vec(0, 2))
        elif char == "v":
            return cls(pos, Vec(0, 3), pos)

    @property
    def type(self):
        return "lava"

    def collide(self,state):
        state.decrease_player_life()
        return GameState(state.level, state.actors, Status.LIFE_DECREASE)

    def update(self,time,state,*args):
        new_pos = self.pos.plus(self.speed.times(time))
        if not state.level.touches(new_pos,self.size,"wall"):
            return Lava(new_pos,self.speed,self.reset)
        elif self.reset:
            return Lava(self.reset,self.speed,self.reset)
        else:
            return Lava(self.pos,self.speed.times(-1))

