import unittest
import main

class TestMain(unittest.TestCase):

    def setUp(self):
        self.board = main.Board()
        self.players = main.Players()

    def test_board_is_3_by_3(self):
        """Ensures the board is 3x3"""

        self.assertEqual(self.board.width, 3)
        self.assertEqual(self.board.height, 3)

    def test_2_players(self):
        """Tests to make sure there's only 2 players"""

        self.assertEqual(self.players.n, 2)

    def test_player_one_goes_first(self):
        """Ensures player 1 goes first"""

        self.assertEqual(self.players.current_player, 1)

    def test_player_two_goes_second(self):
        """Tests to make sure player 2 goes second"""
        self.players.next_player()
        self.assertEqual(self.players.current_player, 2)

    def test_player_one_turn_after_player_two(self):
        """Tests to make sure player 1 goes after player 2"""
        self.players.next_player()
        self.players.next_player()
        self.assertEqual(self.players.current_player, 1)

    def board_is_dstructure_list(self):
        """Ensures the board is a list"""
        self.assertTrue(isinstance(self.board._board, list))

    def board_is_full(self):
        """Forces the board to be full, then checks to make sure it is"""
        # should return true if there is not a 0 in the board.
        board._board = [1] * 9
        self.assertTrue(board._check_if_board_is_empty())

    def board_has_at_least_one_slot_empty(self):
        """Forces the board to have at least one slot empty"""
        board._board = [1] * 9
        board._board[0] = 0
        self.assertFalse(board._check_if_board_is_empty())

    def tearDown(self):
        self.board = main.Board()
        self.players = main.Players()


if __name__ == "__main__":
    unittest.main()
