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


def calculate_numbers(board):
    for row in range(BOARD_SIZE):
        for column in range(BOARD_SIZE):
            if board[row][column] != "*":
                mine_count = count_mines(board, row, column)
                board[row][column] = str(mine_count)


def display_board(board):
    for row in board:
        print(" ".join(row))


def get_player_move():
    while True:
        try:
            row = int(input("Enter row (1-5): "))
            column = int(input("Enter column (1-5): "))

            if 1 <= row <= BOARD_SIZE and 1 <= column <= BOARD_SIZE:
                return row - 1, column - 1

            print("Please enter numbers between 1 and 5.")

        except ValueError:
            print("Please enter numbers only.")


def reveal_cell(game_board, visible_board, row, column):
    visible_board[row][column] = game_board[row][column]


game_board = create_board()
place_mines(game_board)
calculate_numbers(game_board)

visible_board = create_board()

while True:
    print()
    display_board(visible_board)

    row, column = get_player_move()

    reveal_cell(game_board, visible_board, row, column)