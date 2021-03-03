import unittest

from main.actors.player import Player
from main.state.level import Level
from main.state import State


class TestState(unittest.TestCase):
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
        self.state = State.start(Level(level_plan))

    def test_get_player(self):
        self.assertIsInstance(self.state.player,Player)
        self.assertEqual(self.state.player.type,"player")
