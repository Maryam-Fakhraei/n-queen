class ChessBoard:
    def __init__(self, n):
        self.n = n
        self.queen_place_columns = []

    '''
    # define row as index and column as value

    # | 0  1  2  3
    --|-------------
    0 | .  Q  .  .
    1 | .  .  .  Q
    2 | Q  .  .  .
    3 | .  .  Q  .
    queen_place_columns = [1, 3, 0, 2]

    # | 0  1  2  3
    --|-------------
    0 | .  .  Q  .
    1 | Q  .  .  .
    2 | .  .  .  Q
    3 | .  Q  .  .
    queen_place_columns = [2, 0, 3, 1]
    '''

    def is_this_column_safe_in_next_row(self, column):
        # index of next row
        row = len(self.queen_place_columns)

        # check column
        for queen_column in self.queen_place_columns:
            if column == queen_column:
                return False

        # check diagonal
        for queen_row, queen_column in enumerate(self.queen_place_columns):
            if queen_column - queen_row == column - row:
                return False

        # check other diagonal
        for queen_row, queen_column in enumerate(self.queen_place_columns):
            if ((self.n - queen_column) - queen_row == (self.n - column) - row):
                return False
        return True


size = int(input('Enter queen count : '))
board = ChessBoard(size)

status = board.is_this_column_safe_in_next_row()
