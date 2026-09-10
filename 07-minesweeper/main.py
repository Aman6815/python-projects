BOARD_SIZE = 5


def create_board():
    board = []

    for _ in range(BOARD_SIZE):
        row = []

        for _ in range(BOARD_SIZE):
            row.append("□")

        board.append(row)

    return board


def display_board(board):
    for row in board:
        print(" ".join(row))


board = create_board()
display_board(board)