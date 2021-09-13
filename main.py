
class Board:
    width = 3
    height = 3

    # Board Index
    # 0 | 1 | 2
    # 3 | 4 | 5
    # 6 | 7 | 8

    def __init__(self):
        """Instantiates a board object."""
        # None is empty, 1 is player 1, 2 is player 2.
        self._board = [None] * (self.width * self.height)

    def _check_if_board_is_empty(self):
        if 0 in self._board:
            return False
        return True

    def _check_indexes(self, l):
        # If the set is 2 elements, no winner.
        # If the set is 1 element but with None, then no winner.
        check = {self._board[l[0]], self._board[l[1]], self._board[l[2]]}
        if len(check) == 1 and list(check)[0] is not None:
            return True

        return False

    def _check_for_diagonal_win(self):
        """Checks diagonals for winning player"""
        # Check UL to LR
        is_winner = self._check_indexes([0, 4, 8])
        if is_winner:
            return True

        # Check UR to LL
        is_winner = self._check_indexes([2, 4, 6])
        if is_winner:
            return True

        # No winner.
        return False

    def _check_for_horizontal_win(self):
        # Check row 1
        is_winner = self._check_indexes([0, 1, 2])
        if is_winner:
            return True

        # Check row 2
        is_winner = self._check_indexes([3, 4, 5])
        if is_winner:
            return True

        # Check row 3
        is_winner = self._check_indexes([6, 7, 8])
        if is_winner:
            return True

        # No winner.
        return False

    def _check_for_vertical_win(self):
        # Check column 1
        is_winner = self._check_indexes([0, 3, 6])
        if is_winner:
            return True

        # Check row 2
        is_winner = self._check_indexes([1, 4, 7])
        if is_winner:
            return True

        # Check row 3
        is_winner = self._check_indexes([2, 5, 8])
        if is_winner:
            return True

        # No winner.
        return False

class Players:
    n = 2 # 2 players
    current_player = 1 # 1 for player 1, 2 for player 2.

    def next_player(self):
        """Switches players"""

        if self.current_player == 1:
            self.current_player = 2
        else:
            self.current_player = 1
