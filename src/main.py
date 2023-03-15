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

size = int(input('Enter queen count : '))
board = ChessBoard(size)