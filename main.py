
class Board:
    width = 3
    height = 3

    # Board Index
    # 0 | 1 | 2
    # 3 | 4 | 5
    # 6 | 7 | 8

    def __init__(self):
        """Instantiates a board object."""
        # 0 is empty, 1 is player 1, 2 is player 2.
        self._board = [0] * (self.width * self.height)

    def _check_if_board_is_empty(self):
        if 0 in self._board:
            return False
        return True

    def _check_for_diagonal_win(self):
        pass

    def _check_for_horizontal_win(self):
        pass

    def _check_for_vertical_win(self):
        pass

class Players:
    n = 2 # 2 players
    current_player = 1 # 1 for player 1, 2 for player 2.

    def next_player(self):
        """Switches players"""

        if self.current_player == 1:
            self.current_player = 2
        else:
            self.current_player = 1
