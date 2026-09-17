from game import get_replay_choice, play_game


def main():
    while True:
        play_game()

        choice = get_replay_choice()

        if choice == "n":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()