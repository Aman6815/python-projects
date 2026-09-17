import random


BOARD_SIZE = 5
NUMBER_OF_MINES = BOARD_SIZE

HIDDEN_CELL = "□"
MINE = "*"
FLAG = "⚑"


def create_board():
    board = []

    for _ in range(BOARD_SIZE):
        row = []

        for _ in range(BOARD_SIZE):
            row.append("□")

        board.append(row)

    return board


def validate_game_settings():
    total_cells = BOARD_SIZE * BOARD_SIZE

    if BOARD_SIZE < 2:
        raise ValueError("Board size must be at least 2.")

    if NUMBER_OF_MINES < 1:
        raise ValueError("There must be at least 1 mine.")

    if NUMBER_OF_MINES >= total_cells:
        raise ValueError("Number of mines must be less than the number of cells.")


def get_neighbors(row, column):
    neighbors = []

    for row_offset in (-1, 0, 1):
        for column_offset in (-1, 0, 1):
            neighbor_row = row + row_offset
            neighbor_column = column + column_offset

            if (
                0 <= neighbor_row < BOARD_SIZE
                and 0 <= neighbor_column < BOARD_SIZE
                and (neighbor_row, neighbor_column) != (row, column)
            ):
                neighbors.append((neighbor_row, neighbor_column))

    return neighbors


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

    for neighbor_row, neighbor_column in get_neighbors(row, column):
        if board[neighbor_row][neighbor_column] == "*":
            mine_count += 1

    return mine_count


def calculate_numbers(board):
    for row in range(BOARD_SIZE):
        for column in range(BOARD_SIZE):
            if board[row][column] != "*":
                mine_count = count_mines(board, row, column)
                board[row][column] = str(mine_count)


def setup_game():
    validate_game_settings()

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


def get_player_action():
    while True:
        choice = input("Choose action (1=reveal, 2=flag): ")

        if choice in ("1", "2"):
            return choice

        print("Please enter 1 or 2.")


def get_replay_choice():
    while True:
        choice = input("Play again? (y/n): ").lower()

        if choice in ("y", "n"):
            return choice

        print("Please enter y or n.")


def can_reveal(visible_board, row, column):
    return visible_board[row][column] == "□"


def reveal_cell(game_board, visible_board, row, column):
    if not can_reveal(visible_board, row, column):
        return

    visible_board[row][column] = game_board[row][column]

    if game_board[row][column] != "0":
        return

    for neighbor_row, neighbor_column in get_neighbors(row, column):
        if (
            game_board[neighbor_row][neighbor_column] != "*"
            and visible_board[neighbor_row][neighbor_column] == "□"
        ):
            reveal_cell(
                game_board,
                visible_board,
                neighbor_row,
                neighbor_column
            )


def toggle_flag(visible_board, row, column):
    if visible_board[row][column] == "□":
        visible_board[row][column] = "⚑"
        print("Cell flagged.")

    elif visible_board[row][column] == "⚑":
        visible_board[row][column] = "□"
        print("Flag removed.")

    else:
        print("You cannot flag a revealed cell.")


def reveal_all_mines(game_board, visible_board):
    for row in range(BOARD_SIZE):
        for column in range(BOARD_SIZE):
            if game_board[row][column] == "*":
                visible_board[row][column] = "*"


def has_won(game_board, visible_board):
    revealed_safe_cells = 0

    for row in range(BOARD_SIZE):
        for column in range(BOARD_SIZE):
            if (
                game_board[row][column] != "*"
                and visible_board[row][column] != "□"
                and visible_board[row][column] != "⚑"
            ):
                revealed_safe_cells += 1

    total_safe_cells = BOARD_SIZE * BOARD_SIZE - NUMBER_OF_MINES

    return revealed_safe_cells == total_safe_cells


def play_game():
    game_board, visible_board = setup_game()
    moves = 0

    while True:
        display_board(visible_board)
        print(f"Moves: {moves}")

        row, column = get_player_move()
        action = get_player_action()

        if action == "2":
            toggle_flag(visible_board, row, column)
            continue

        if not can_reveal(visible_board, row, column):
            print("That cell cannot be revealed. Choose another cell.")
            continue

        moves += 1

        if game_board[row][column] == "*":
            visible_board[row][column] = "*"
            reveal_all_mines(game_board, visible_board)

            display_board(visible_board)
            print(f"💣 Game over! You hit a mine after {moves} moves.")
            break

        reveal_cell(game_board, visible_board, row, column)

        if has_won(game_board, visible_board):
            display_board(visible_board)
            print(f"🏆 Congratulations! You won in {moves} moves.")
            break


while True:
    play_game()

    choice = get_replay_choice()

    if choice == "n":
        print("Thanks for playing!")
        break