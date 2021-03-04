import math
from random import random

from main.settings import Status
from main.model.gamestate import GameState
from main.model.vec import Vec


class Coin:
    size = Vec(0.6, 0.6)
    wobble_speed = 8
    wobble_dist = 0.1

    def __init__(self, pos, base_pos, wobble):
        self.pos = pos
        self.base_pos = base_pos
        self.wobble = wobble

    @classmethod
    def create(cls, pos, char=None):
        base_pos = pos.plus(Vec(0.2, 0.1))
        return Coin(pos, base_pos, random() * math.pi * 2)

    @property
    def type(self):
        return "coin"

    def collide(self, state):
        untouched_char = list(filter(lambda x: x != self, state.actors))
        status = state.status
        if not any((x.type == "coin" for x in untouched_char)):
            status = Status.WON
        return GameState(state.level, untouched_char, status)

    def update(self,time,*args):
        wobble = self.wobble + time*self.wobble_speed
        wobble_pos = math.sin(wobble)*self.wobble_dist
        return Coin(self.base_pos.plus(Vec(0,wobble_pos)),
                    self.base_pos,wobble)