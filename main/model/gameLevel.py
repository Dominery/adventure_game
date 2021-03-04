import math

from main.model.actors.coin import Coin
from main.model.actors.lava import Lava
from main.model.actors.player import Player
from main.model.vec import Vec

levelChars = {
    ".": "empty", "#": "wall", "+": "lava", "@": Player, "o": Coin,
    "=": Lava, "|": Lava, "v": Lava,"&":"store"
}


class Level:
    def __init__(self, plan: str):
        rows = plan.strip().split("\n")
        rows = list(map(lambda x: list(x.strip()), rows))

        self.height = len(rows)
        self.width = len(rows[0])
        self.start_actors = []
        self.rows = self._change_chars_to_obj(rows)

    def _change_chars_to_obj(self, rows):
        obj_info = []
        for y in range(self.height):
            obj_info_row = []
            for x in range(self.width):
                char = rows[y][x]
                obj_type = levelChars[char]
                if isinstance(obj_type, str):
                    obj_info_row.append(obj_type)
                    continue
                self.start_actors.append(obj_type.create(Vec(x, y), char))
                obj_info_row.append("empty")
            obj_info.append(obj_info_row)
        return obj_info

    def touches(self, pos, size, type):
        x_start = math.floor(pos.x)
        x_end = math.ceil(pos.x + size.x)
        y_start = math.floor(pos.y)
        y_end = math.ceil(pos.y + size.y)

        for y in range(y_start, y_end):
            for x in range(x_start, x_end):
                is_outside = x < 0 or x >= self.width or y < 0 or y >= self.height
                here = "wall" if is_outside else self.rows[y][x]
                if here == type:
                    return True
        return False
