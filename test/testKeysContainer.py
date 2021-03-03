import unittest

from main.component.keysContainer import KeysContainer


class KeysContainerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.keys = KeysContainer(["ArrowLeft","ArrowRight"])

    def test_get_attr(self):
        self.assertEqual(self.keys.ArrowRight, False)

    def test_set_attr(self):
        self.assertFalse(self.keys.ArrowLeft)
        self.keys["ArrowLeft"] = True
        self.assertTrue(self.keys["ArrowLeft"])

    def test_in(self):
        self.assertTrue("ArrowLeft" in self.keys)


if __name__ == '__main__':
    unittest.main()
