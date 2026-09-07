class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]

    def print_board(self):
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    def make_move(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter
            return True

        return False


game = TicTacToe()

game.make_move(4, "X")
game.make_move(0, "O")

game.print_board()