import math
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
        if len(game.available_moves()) == 9:
            return random.choice(game.available_moves())

        return self.minimax(game, self.letter, -math.inf, math.inf)["position"]

    def minimax(self, state, player, alpha, beta):
        max_player = self.letter  # the AI itself
        other_player = "O" if player == "X" else "X"

        # Base case: the last move made (by other_player) won the game
        if state.current_winner == other_player:
            score = (
                (state.num_empty_squares() + 1)
                if other_player == max_player
                else -(state.num_empty_squares() + 1)
            )
            return {"position": None, "score": score}

        # Base case: no squares left, it's a draw
        elif not state.empty_squares():
            return {"position": None, "score": 0}

        if player == max_player:
            best = {"position": None, "score": -math.inf}
        else:
            best = {"position": None, "score": math.inf}

        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player, alpha, beta)

            # undo the simulated move (backtracking)
            state.board[possible_move] = " "
            state.current_winner = None
            sim_score["position"] = possible_move

            if player == max_player:
                if sim_score["score"] > best["score"]:
                    best = sim_score
                alpha = max(alpha, best["score"])
            else:
                if sim_score["score"] < best["score"]:
                    best = sim_score
                beta = min(beta, best["score"])

            if beta <= alpha:
                break  # prune: opponent already has a better option elsewhere

        return best