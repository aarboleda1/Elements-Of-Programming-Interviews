"""
Tic tac toe
- print board
- ask user for board

create a simple AI to populate board
AI should:
1) go in an open spot
2) go in an open spot

Board
    Manage the state of the board

    attributes
        _board
    actions
        - add_move
        - validate_move
        - is_board_full



Game
    Manage the state of the game
    attributes
        - player1
        - player2
    actions
        - play
        - check_game_over
        - switch_player



Player
    Manages all player functionality

    attributes
        - name
    actions
        make_move():
            while True:
                get user input
                board.make_move
        get_user_input()
        validate_user_input()
"""
import time

class Board:
    def __init__(self):
        self._board = {}
        self._create_board()

    def _create_board(self):
        for row in range(3):
            for col in range(3):
                self._board[(row, col)] = "-"
        self.print_board()

    def print_board(self):
        keys = sorted(self._board.keys())
        print("Board")
        for i in range(0, 9, 3):
            row = keys[i : i + 3]
            row_vals = ""
            for cell in row:
                row_vals += "|" + self._board[cell]
            print(row_vals[1:])
        print("------------------------------\n")

    def mark_cell(self, player, coord):
        self._board[coord] = player
        self.print_board()

    def is_full(self):
        for coord, val in self._board.items():
            if self._board[coord] == "-":
                return False
        return True

    def has_player_won(self, player):
        # rows
        for i in range(3):
            horizontal = [
                self._board[(row, col)] for row, col in self._board.keys() if row == i
            ]
            # columns
            vertical = [self._board[(row, col)] for row, col in self._board.keys() if col == i]
            diagonals = [self._board[(row, col)] for row, col in sorted(self._board.keys()) if row == col]
            c = horizontal.count(player)
            if horizontal.count(player) == 3 or vertical.count(player) == 3 or diagonals.count(player) == 3:
                return True
        return False

    def find_empty_cell(self):
        for coord, val in self._board.items():
            if self._board[coord] == "-":
                return coord
        return False


class Game:
    def __init__(self):
        self.player_one = "X"
        self.player_two = "O"
        self.player_move = self.player_one
        print(
        f"""Welcome to tic tac toe, you are player X. \n
        You will be playing against our most advanced robot \n

        To make a move, enter a coordinate like so: 0,0 \n

        Good luck!\n
        """)
        self.board = Board()

    def play(self):
        while not self.board.is_full():
            if self.player_move == "X":
                print("Your Move!\n")
                user_input = input("Enter coordinates: ")
                user_input = user_input.split(",")
                coord = (int(user_input[0]), int(user_input[1]))
            else:
                print("The AI is thinking... ")
                time.sleep(3)
                print("Almost ready....")
                time.sleep(2)
                coord = self.board.find_empty_cell()
            self.board.mark_cell(self.player_move, coord)
            if self.board.has_player_won(self.player_move):
                break
            self.player_move = (
                self.player_two
                if self.player_move == "X"
                else self.player_one
            )
        print("Game over!")


if __name__ == "__main__":
    print("Starting Tic Tac Toe! \n")
    game = Game()
    game.play()
