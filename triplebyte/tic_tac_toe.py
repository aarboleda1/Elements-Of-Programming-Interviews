
"""
- print board
- add token to board

Step 2
"""
class TicTacToe:
    def __init__(self):
        self.board = {}
        self.init_board()


    def init_board(self):
        for row in range(3):
            for col in range(3):
                self.board[(row, col)] = "-"

    def print_board(self):
        coords = list(self.board.keys())
        coords.sort(key=lambda coord: coord[0])
        print("\n")
        wall = "|"
        print(coords)
        for i in range(0, 9, 3):
            row = (self.board[coords[i]] + wall +
                self.board[coords[i + 1]] + wall +
                self.board[coords[i + 2]])
            print(row)
        """
        0,0, (0,1) (0,2)
        """

    def add_token(self, player, coords):
        if self.valid_move(coords):
            self.board[coords] = player

    def board_full(self):
        for coord, player in self.board.items():
            if player == "-":
                return False
        return True

    def make_AI_move(self):
        if self.board_full():
            raise Exception("Board is full!")

        for coord, player in self.board.items():
            if player == "-":
                self.board[coord] = "O"
                return

    def valid_move(self, coords): # TODO, throw Ex
        return True

if __name__ == "__main__":
    print("hello starting")
    game = TicTacToe()
    game.print_board()
    while True:
        game.make_AI_move()
        game.print_board()
