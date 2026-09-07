class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]

    def print_board(self):
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    def available_moves(self):
        return [i for i, square in enumerate(self.board) if square == " "]

    def make_move(self, square, letter):
        if square in self.available_moves():
            self.board[square] = letter
            return True

        return False


game = TicTacToe()

game.make_move(4, "X")
game.make_move(0, "O")

print("Available moves:", game.available_moves())
game.print_board()