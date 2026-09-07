from player import HumanPlayer, RandomComputerPlayer


class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    def available_moves(self):
        return [i for i, square in enumerate(self.board) if square == " "]

    def empty_squares(self):
        return " " in self.board

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


def play_game(x_player, o_player):
    game = TicTacToe()
    letter = "X"

    while game.empty_squares():
        game.print_board()

        player = x_player if letter == "X" else o_player
        square = player.get_move(game)

        if game.make_move(square, letter):
            if game.current_winner:
                game.print_board()
                print(f"{letter} wins!")
                return

            letter = "O" if letter == "X" else "X"

    game.print_board()
    print("It's a tie!")


x_player = HumanPlayer("X")
o_player = RandomComputerPlayer("O")

play_game(x_player, o_player)