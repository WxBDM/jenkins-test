import unittest
import main

class TestMain(unittest.TestCase):

    def setUp(self):
        self.board = main.Board()
        self.players = main.Players()

    def test_board_is_3_by_3(self):
        self.assertEqual(self.board.width, 3)
        self.assertEqual(self.board.height, 3)

    def test_2_players(self):
        self.assertEqual(self.players.n, 2)

    def test_this_will_fail(self):
        self.assertEqual(2, 3)


if __name__ == "__main__":
    unittest.main()
