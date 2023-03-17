from termcolor import *
from time import *

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
    
    def place_in_next_row(self, column):
        self.queen_place_columns.append(column)
    
    def display(self):
        for row in range(self.n):
            for column in range(self.n):
                if column == self.queen_place_columns[row]:
                    print('Q', end=' ')
                else:
                    print('.', end=' ')
            print()
    
    def remove_in_current_row(self):
        return self.queen_place_columns.pop()

def solve_n_queen(n):
    board = ChessBoard(n)
    number_of_solutions = 0

    row = 0
    column = 0
    # iterate over rows of board
    while True:
        # place queen in next row
        while column < n:
            if board.is_this_column_safe_in_next_row(column):   
                board.place_in_next_row(column)
                row += 1
                column = 0
                break
            else:
                column += 1

        # if could not find column to place in or if board is full
        if (column == n or row == n):
            # if board is full, we have a solution
            if row == n:
                sleep(1)
                board.display()
                print()
                number_of_solutions += 1
                board.remove_in_current_row()
                row -= 1

                # now backtrack
            try:
                prev_column = board.remove_in_current_row()
            except IndexError:
                # all queens removed
                # thus no more possible configurations
                break
            # try previous row again
            row -= 1
            # start checking at column = (1 + value of column in previous row)
            column = 1 + prev_column

    sleep(1)
    print(colored(">>> Number of solutions: %s \n" %(number_of_solutions), "cyan"))
    print("-----------------------------------------------")

# Communication with the user
print(colored("===> Welcome to N Queen Solver <=== \n", "light_yellow", attrs=["bold"]))

# Get disk count from user
print("-----------------------------------------------")
size = int(input(colored('Enter Queen count : ', "light_green")))
print()

# Run until user enter 0
while size != 0:
    solve_n_queen(size)
    sleep(1)
    size = int(input(colored("Enter queen count (enter 0 if you want to exit) : ", "light_green")))
    print()
    
# Developers
print(colored("\nThank you for choosing us :)\n>>>Developed by Maryam Fakhraei and Amirhossein Naseri<<<", "light_magenta"))