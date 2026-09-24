def find_next_empty(puzzle):
    """Return the position of the first empty cell."""

    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == -1:
                return row, col

    return None, None


def is_valid(puzzle, guess, row, col):
    """Return True if a guess is valid at the given position."""

    # Check the row.
    if guess in puzzle[row]:
        return False

    # Check the column.
    for current_row in range(9):
        if puzzle[current_row][col] == guess:
            return False

    # Find the top-left corner of the 3x3 box.
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    # Check the 3x3 box.
    for current_row in range(row_start, row_start + 3):
        for current_col in range(col_start, col_start + 3):
            if puzzle[current_row][current_col] == guess:
                return False

    return True


example_board = [
    [3, 9, -1, -1, 5, -1, -1, -1, -1],
    [-1, -1, -1, 2, -1, -1, -1, -1, 5],
    [-1, -1, -1, 7, 1, 9, -1, 8, -1],

    [-1, 5, -1, -1, 6, 8, -1, -1, -1],
    [2, -1, 6, -1, -1, 3, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, 4],

    [5, -1, -1, -1, -1, -1, -1, -1, -1],
    [6, 7, -1, 1, -1, 5, -1, 4, -1],
    [1, -1, 9, -1, -1, -1, 2, -1, -1]
]


row, col = find_next_empty(example_board)

print("First empty cell:", row, col)
print("Is 4 valid?", is_valid(example_board, 4, row, col))
print("Is 3 valid?", is_valid(example_board, 3, row, col))