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


def setup_game():
    game_board = create_board()
    place_mines(game_board)
    calculate_numbers(game_board)

    visible_board = create_board()

    return game_board, visible_board


def display_board(board):
    print()
    print("    " + " ".join(str(column) for column in range(1, BOARD_SIZE + 1)))
    print("   " + "--" * BOARD_SIZE)

    for row_number, row in enumerate(board, start=1):
        print(f"{row_number} | " + " ".join(row))


def get_player_move():
    while True:
        try:
            row = int(input(f"Enter row (1-{BOARD_SIZE}): "))
            column = int(input(f"Enter column (1-{BOARD_SIZE}): "))

            if 1 <= row <= BOARD_SIZE and 1 <= column <= BOARD_SIZE:
                return row - 1, column - 1

            print(f"Please enter numbers between 1 and {BOARD_SIZE}.")

        except ValueError:
            print("Please enter numbers only.")


def reveal_cell(game_board, visible_board, row, column):
    visible_board[row][column] = game_board[row][column]


def has_won(visible_board):
    for row in visible_board:
        for cell in row:
            if cell == "□":
                return False

    return True


def play_game():
    game_board, visible_board = setup_game()
    moves = 0

    while True:
        display_board(visible_board)
        print(f"Moves: {moves}")

        row, column = get_player_move()

        if visible_board[row][column] != "□":
            print("That cell has already been revealed. Choose another cell.")
            continue

        moves += 1

        if game_board[row][column] == "*":
            visible_board[row][column] = "*"

            display_board(visible_board)
            print(f"💣 Game over! You hit a mine after {moves} moves.")
            break

        reveal_cell(game_board, visible_board, row, column)

        if has_won(visible_board):
            display_board(visible_board)
            print(f"🏆 Congratulations! You won in {moves} moves.")
            break


while True:
    play_game()

    choice = input("Play again? (y/n): ").lower()

    if choice != "y":
        print("Thanks for playing!")
        break