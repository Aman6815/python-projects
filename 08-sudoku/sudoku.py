def validate_puzzle(puzzle):
    """Raise ValueError if the puzzle has an invalid structure."""

    if len(puzzle) != 9:
        raise ValueError("Puzzle must contain exactly 9 rows.")

    for row in puzzle:
        if len(row) != 9:
            raise ValueError("Each row must contain exactly 9 values.")

        for value in row:
            if not isinstance(value, int):
                raise ValueError("Puzzle values must be integers.")

            if value < -1 or value > 9:
                raise ValueError("Puzzle values must be between -1 and 9.")


def find_next_empty(puzzle):
    """Return the position of the first empty cell."""

    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == -1:
                return row, col

    return None, None


def is_valid(puzzle, guess, row, col):
    """Return True if a guess is valid at the given position."""

    if guess in puzzle[row]:
        return False

    for current_row in range(9):
        if puzzle[current_row][col] == guess:
            return False

    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for current_row in range(row_start, row_start + 3):
        for current_col in range(col_start, col_start + 3):
            if puzzle[current_row][current_col] == guess:
                return False

    return True


def solve_sudoku(puzzle):
    """Validate and solve the puzzle using backtracking."""

    validate_puzzle(puzzle)

    return _solve(puzzle)


def _solve(puzzle):
    """Solve a validated puzzle using backtracking."""

    row, col = find_next_empty(puzzle)

    if row is None:
        return True

    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess

            if _solve(puzzle):
                return True

            puzzle[row][col] = -1

    return False


def print_board(puzzle):
    """Print the Sudoku board in a readable format."""

    for row in puzzle:
        print(" ".join(str(value) for value in row))


def main():
    """Run the Sudoku solver with an example puzzle."""

    puzzle = [
        [3, 9, -1, -1, 5, -1, -1, -1, -1],
        [-1, -1, -1, 2, -1, -1, -1, -1, 5],
        [-1, -1, -1, 7, 1, 9, -1, 8, -1],

        [-1, 5, -1, -1, 6, 8, -1, -1, -1],
        [2, -1, 6, -1, -1, 3, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, 4],

        [5, -1, -1, -1, -1, -1, -1, -1, -1],
        [6, 7, -1, 1, -1, 5, -1, 4, -1],
        [1, -1, 9, -1, -1, -1, 2, -1, -1],
    ]

    print("Original puzzle:")
    print_board(puzzle)

    print("\nSolving...")

    if solve_sudoku(puzzle):
        print("\nSolved puzzle:")
        print_board(puzzle)
    else:
        print("\nThis Sudoku has no solution.")


if __name__ == "__main__":
    main()