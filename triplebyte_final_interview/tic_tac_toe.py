class Board:
    def __init__(self):
        self.board = {}

    def init_board(self):
        for x in range(3):
            for y in range(3):
                self.board[(x,y)] = "-"

    def add_token(self, coordinate, token):
        self.board[coordinate] = token

    def print_board(self):
        keys = sorted(self.board.items())
        for i in range(0, len(keys), 3):
            row_to_print = ""
            for j in range(i, i + 3):
                row_to_print += "|" + keys[j][1]
            print(row_to_print[1:])

    def is_board_full(self):
        for coord, token in self.board.items():
            if token == "-":
                return False
        return True

def make_ai_move(board):
    coordinate = None
    for coord, token in sorted(board.board.items()):
        if token == "-":
            coordinate = coord
    print(coordinate)
    if not coordinate:
        raise Exception("Board is full")
    board.add_token(coordinate, "O")

class Game:
    def __init__(self, board):
        self.board = board

    def play(self):
        player_turn = player_one = "X"  # user
        player_two = "O" # AI
        while not self.board.is_board_full():
            if player_turn == player_one:
                coord = self.get_valid_user_input()
                coord = (int(user_input[0]), int(user_input[2]))
                self.board.add_token(coord, player_turn)
            else:
                make_ai_move(self.board)

            if player_turn == player_one:
                player_turn = player_two
            else:
                player_turn = player_one
            self.board.print_board()

    def get_valid_user_input(self):
        user_input = input("Input your coordinates: ")
        coord = (int(user_input[0]), int(user_input[2]))
        return coord



if __name__ == "__main__":
    board = Board()
    board.init_board()
    game = Game(board)
    game.play()
    # make_ai_move(board)
    board.print_board()
