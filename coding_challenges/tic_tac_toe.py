import re

EMPTY = '-'
PLAYER_X = 'X'
PLAYER_O = 'O'


def init_board(n):
    board = {}
    for x in range(n):
        for y in range(n):
            board[(x, y)] = EMPTY
    return board


def print_board(board):
    print('\n')
    for coord in sorted(board.keys()):
        x, y = coord
        if y == 0 and x != 0:           # if is new row
            print('\n' + '-' * 2* len(board))

        val = board[coord]
        if val is not EMPTY:
            print("  %s  |" % (val), end="")
        else:
            print("(%1d,%1d)|" % (coord), end="")
    print('\n')


def place_piece(board, coord, player):
    if coord in board.keys() and board[coord] is EMPTY:
        board[coord] = player
        return True
    else:
        return False


def has_won(board, size, player):
    for n in range(size):
        rows = [board[(x, y)] for x, y in sorted(board.keys()) if n is x]
        cols = [board[(x, y)] for x, y in sorted(board.keys()) if n is y]
        diagonals = [board[(x, y)] for x, y in sorted(board.keys()) if x is y]
        if rows.count(player) is size or cols.count(player) is size or diagonals.count(player) is size:
            return True
    return False

def board_full(board):
    return list(board.values()).count(EMPTY) == 0

def game_ended(board, size):
    return board_full(board) or has_won(board, size, PLAYER_X) or has_won(board, size, PLAYER_O)

def game_winner(board, size):
    if has_won(board, size, PLAYER_X):
        return PLAYER_X
    elif has_won(board, size, PLAYER_O):
        return PLAYER_O
    elif board_full(board):
        return None

def valid_move(user_in):
    user_in = user_in.strip()
    matches = re.match(r"[0-9]+\s*,\s*[0-9]+", user_in)
    if matches is not None:
        return tuple(map(int, user_in.split(',')))
    else:
        return False

def game():
    size = 3
    board = init_board(size)
    print("\n*****************************************")
    print("Let's play some tic tac toe!")
    print("X: Player X, O: Player O, (x,y): Empty spot")
    print("Enter coordinate in empty spot to fill it\n")

    print_board(board)
    turn = PLAYER_O

    while(not game_ended(board, size)):
        user_in = input("Player " +  turn + ", place your piece: ")
        coord = valid_move(user_in)

        if coord and place_piece(board, coord, turn):
            print_board(board)
            #switch turns
            turn = PLAYER_X  if turn is PLAYER_O else PLAYER_O
        else:
            print("Invalid move.")

    winner = game_winner(board, size)
    if winner is not None:
        print('Game ended! Player %s won!' % winner)
    else:
        print('There was a tie. No one won :)')

def test():
    size = 3
    board = init_board(size)
    print_board(board)
    assert place_piece(board, (0, 0), PLAYER_X) == True
    assert place_piece(board, (0, 0), PLAYER_X) == False
    assert place_piece(board, (1, 1), PLAYER_O) == True

    assert place_piece(board, (0, 1), PLAYER_X) == True
    assert place_piece(board, (0, 2), PLAYER_X) == True
    assert has_won(board, size, PLAYER_X) == True
    assert has_won(board, size, PLAYER_O) == False
    print_board(board)

    board = init_board(size)

    assert place_piece(board, (0, 0), PLAYER_O) == True
    assert place_piece(board, (1, 1), PLAYER_O) == True
    assert place_piece(board, (2, 2), PLAYER_O) == True
    assert has_won(board, size, PLAYER_O) == True

    print_board(board)

    assert valid_move('3,4') == (3,4)
    assert valid_move('3,  4') == (3,4)
    assert valid_move('a,4') == False
    assert valid_move('33,49') == (33,49)
    assert valid_move('33 , 49') == (33,49)
    assert valid_move('fsdfdsf') == False
    assert valid_move('fsdm,fdsf') == False
    assert valid_move('fsdm,   fdsf') == False
    print('tests pass')

test()
game()
