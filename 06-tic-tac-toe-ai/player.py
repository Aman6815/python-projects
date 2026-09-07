import random


class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class HumanPlayer(Player):
    def get_move(self, game):
        while True:
            try:
                square = int(
                    input(f"{self.letter}'s turn. Choose a square (0-8): ")
                )

                if square in game.available_moves():
                    return square

                print("That square is not available. Try again.")

            except ValueError:
                print("Please enter a number.")


class RandomComputerPlayer(Player):
    def get_move(self, game):
        return random.choice(game.available_moves())


class SmartComputerPlayer(Player):
    def get_move(self, game):
        if 4 in game.available_moves():
            return 4

        return random.choice(game.available_moves())