import random


BOARD_SIZE = 5
NUMBER_OF_MINES = 5


def create_board():
    board = []

    for _ in range(BOARD_SIZE):
        row = []

        for _ in range(BOARD_SIZE):
            row.append("□")

        board.append(row)

    return board


def place_mines(board):
    mines_placed = 0

    while mines_placed < NUMBER_OF_MINES:
        row = random.randrange(BOARD_SIZE)
        column = random.randrange(BOARD_SIZE)

        if board[row][column] == "□":
            board[row][column] = "*"
            mines_placed += 1


def display_board(board):
    for row in board:
        print(" ".join(row))


board = create_board()
place_mines(board)
display_board(board)