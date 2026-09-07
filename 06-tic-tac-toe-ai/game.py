class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    def available_moves(self):
        return [i for i, square in enumerate(self.board) if square == " "]

    def make_move(self, square, letter):
        if square in self.available_moves():
            self.board[square] = letter

            if self.winner(square, letter):
                self.current_winner = letter

            return True

        return False

    def winner(self, square, letter):
        row_index = square // 3
        row = self.board[row_index * 3:(row_index + 1) * 3]

        if all(square == letter for square in row):
            return True

        column_index = square % 3
        column = [self.board[column_index + i * 3] for i in range(3)]

        if all(square == letter for square in column):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            diagonal2 = [self.board[i] for i in [2, 4, 6]]

            if all(square == letter for square in diagonal1):
                return True

            if all(square == letter for square in diagonal2):
                return True

        return False


game = TicTacToe()

game.make_move(0, "X")
game.make_move(3, "O")
game.make_move(1, "X")
game.make_move(4, "O")
game.make_move(2, "X")

game.print_board()
print("Winner:", game.current_winner)