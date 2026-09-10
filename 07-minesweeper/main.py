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


def count_mines(board, row, column):
    mine_count = 0

    for row_offset in (-1, 0, 1):
        for column_offset in (-1, 0, 1):
            neighbor_row = row + row_offset
            neighbor_column = column + column_offset

            if (
                0 <= neighbor_row < BOARD_SIZE
                and 0 <= neighbor_column < BOARD_SIZE
                and board[neighbor_row][neighbor_column] == "*"
            ):
                mine_count += 1

    return mine_count


def display_board(board):
    for row in board:
        print(" ".join(row))


board = create_board()
place_mines(board)

display_board(board)

print(count_mines(board, 0, 0))
print(count_mines(board, 2, 2))