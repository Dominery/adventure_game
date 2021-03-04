import unittest

from main.model.gameLevel import Level
from main.model.vec import Vec


class TestLevel(unittest.TestCase):
    def setUp(self) -> None:
        level_plan = """
        ......................
        ..#................#..
        ..#..............=.#..
        ..#.........o.o....#..
        ..#.@......#####...#..
        ..#####............#..
        ......#++++++++++++#..
        ......##############..
        ......................"""
        self.level = Level(level_plan)

    def test_change_char_to_obj(self):
        self.assertEqual(self.level.rows[1][2],"wall")
        self.assertEqual(self.level.rows[-3][-4],"lava")
        self.assertIsInstance(self.level.start_actors[0],object)

    def test_touches(self):
        char_type = [Vec(-1,1),Vec(1,1),"player"]
        is_touch = self.level.touches(*char_type)
        self.assertFalse(is_touch)
        char_type[-1]="wall"
        self.assertTrue(self.level.touches(*char_type))
