
class Board:
    width = 3
    height = 3

    def __init__(self):
        """Instantiates a board object."""
        # 0 is empty, 1 is player 1, 2 is player 2.
        self._board = [0] * (width * height)

    def _check_if_board_is_empty(self):
        if 0 in self._board:
            return False
        return True

class Players:
    n = 2 # 2 players
    which_player = 1 # 1 for player 1, 2 for player 2.

    def next_player(self):
        """Switches players"""

        if self.which_player == 1:
            self.which_player = 2
        else:
            self.which_player = 1
