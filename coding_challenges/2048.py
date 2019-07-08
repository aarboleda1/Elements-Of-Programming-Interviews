"""
Goal is to get the user to 2048

1) 1st construct the board with two tiles of value 4
2)
| | | | |

A move will be a direction

[
    [ 2, 2, 2, 2], -> [4, 4, 0, 0]
    [],
    [],
    []
]

<-
[
    [ 4, 2, 2, 2],
    [],
    [],
    []
]

User will make an action

"""
import random
MOVES = set(["u", "d", "r", "l"])

class Game:
    def __init__(self, size):
        self.board = [[0 for i in range(size)] for i in range(size)]
        self.size = size

    def play(self):
        self.print_board()
        user_input = self.get_user_input()
        if user_input == "u":
            # start at bottom
            self.shift_up()
        elif user_input == "d":
            pass
        elif user_input == "l":
            pass
        elif user_input == "r":
            pass
        self.print_board()

    def shift_up(self):
        row_idx = len(self.board) - 1
        while row_idx > 0:
            for col_idx in range(self.size):
                # case 1
                if (self.board[row_idx][col_idx] and
                    self.board[row_idx - 1][col_idx] == self.board[row_idx][col_idx]
                ):
                    self.board[row_idx - 1][col_idx] = self.board[row_idx - 1][col_idx] * 2
                    self.board[row_idx][col_idx] = 0
                while row_idx > 0 and self.board[row_idx - 1][col_idx] == 0:
                    self.board[row_idx - 1][col_idx] = self.board[row_idx][col_idx]
                    row_idx -= 1


            row_idx -= 1

def move_left(self, col):
    new_col = [0, 0, 0, 0]
    write_idx = 0
    previous = None
    for i in range(len(col)):
        if col[i] != 0: # number different from zero
            if previous == None:
                previous = col[i]
            else:
                if previous == col[i]:
                    new_col[write_idx] = 2 * col[i]
                    write_idx += 1
                    previous = None
                else:
                    new_col[write_idx] = previous
                    write_idx += 1
                    previous = col[i]
    if previous != None:
        new_col[write_idx] = previous
    return new_col

    def get_start_cells(self):
        cells = [(x,y) for x in range(self.size) for y in range(self.size)]
        random_cell1 = random.randint(0, (self.size * self.size) - 1)
        random_cell2 = random.randint(0, (self.size * self.size) - 1)
        while random_cell2 == random_cell1:
            random_cell2 = random.randint(0, (self.size * self.size) - 1)
        return [cells[random_cell1], cells[random_cell2]]

    def print_board(self):
        start_cells = self.get_start_cells()
        for row_idx, row in enumerate(self.board):
            formatted_row = ""
            for col_idx, val in enumerate(row):
                if (row_idx, col_idx) in start_cells:
                    val = 2
                formatted_row += "|" + ("_" if not val else str(val))
            print(formatted_row + "|")

    def get_user_input(self):
        move = input("Type in u, d, r, l:")
        if move.lower() not in MOVES:
            print("invalid move!")
        return move


if __name__ == "__main__":
    game = Game(4)
    # game.get_user_input()
    # game.print_board()
    print(game.move_left([0, 2, 2, 0]))
