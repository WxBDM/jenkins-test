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

    def test_board_is_dstructure_list(self):
        """Ensures the board is a list"""
        self.assertTrue(isinstance(self.board._board, list))

    def test_board_is_full(self):
        """Forces the board to be full, then checks to make sure it is"""
        # should return true if there is not a 0 in the board.
        self.board._board = [1] * 9
        self.assertTrue(self.board._check_if_board_is_empty())

    def test_board_has_at_least_one_slot_empty(self):
        """Forces the board to have at least one slot empty"""
        self.board._board = [1] * 9
        self.board._board[0] = 0
        self.assertFalse(self.board._check_if_board_is_empty())

        # Board Index
        # 0 | 1 | 2
        # 3 | 4 | 5
        # 6 | 7 | 8

    def test_column_1_is_winner(self):
        """Forces first column as a winner"""
        self.board._board[0], self.board._board[3], self.board._board[6] = 1, 1, 1
        self.assertTrue(self.board._check_for_vertical_win())

    def test_column_2_is_winner(self):
        """Forces second column as a winner"""
        self.board._board[1], self.board._board[4], self.board._board[7] = 1, 1, 1
        self.assertTrue(self.board._check_for_vertical_win())

    def test_column_3_is_winner(self):
        """Forces third column as a winner"""
        self.board._board[2], self.board._board[5], self.board._board[8] = 1, 1, 1
        self.assertTrue(self.board._check_for_vertical_win())

    def test_row_1_is_winner(self):
        """Forces first row as a winner"""
        self.board._board[0], self.board._board[1], self.board._board[2] = 1, 1, 1
        self.assertTrue(self.board._check_for_horizontal_win())

    def test_row_2_is_winner(self):
        """Forces second row as a winner"""
        self.board._board[3], self.board._board[4], self.board._board[5] = 1, 1, 1
        self.assertTrue(self.board._check_for_horizontal_win())

    def test_row_3_is_winner(self):
        """Forces third row as a winner"""
        self.board._board[6], self.board._board[7], self.board._board[8] = 1, 1, 1
        self.assertTrue(self.board._check_for_horizontal_win())

    def test_diagonal_1_is_winner(self):
        """Forces forward diagonal as a winner"""
        self.board._board[0], self.board._board[4], self.board._board[8] = 1, 1, 1
        self.assertTrue(self.board._check_for_diagonal_win())

    def test_diagonal_2_is_winner(self):
        """Forces backwards diagonal as a winner"""
        self.board._board[2], self.board._board[4], self.board._board[6] = 1, 1, 1
        self.assertTrue(self.board._check_for_diagonal_win())

    def tearDown(self):
        self.board = main.Board()
        self.players = main.Players()


if __name__ == "__main__":
    unittest.main()
