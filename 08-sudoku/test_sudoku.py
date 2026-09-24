import unittest

from sudoku import find_next_empty, is_valid, solve_sudoku


class TestSudoku(unittest.TestCase):

    def setUp(self):
        self.board = [
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

    def test_find_next_empty(self):
        self.assertEqual(find_next_empty(self.board), (0, 2))

    def test_valid_guess(self):
        self.assertTrue(is_valid(self.board, 4, 0, 2))

    def test_invalid_guess(self):
        self.assertFalse(is_valid(self.board, 3, 0, 2))

    def test_solve_sudoku(self):
        solved = solve_sudoku(self.board)

        self.assertTrue(solved)

        for row in self.board:
            self.assertEqual(set(row), set(range(1, 10)))


if __name__ == "__main__":
    unittest.main()