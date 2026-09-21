from search import binary_search


def get_numbers():
    while True:
        user_input = input("Enter numbers separated by spaces: ")

        try:
            numbers = [int(number) for number in user_input.split()]
        except ValueError:
            print("Invalid input. Please enter whole numbers only.")
            continue

        if not numbers:
            print("Please enter at least one number.")
            continue

        return sorted(numbers)


def get_target():
    while True:
        user_input = input("Enter a number to search for: ")

        try:
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def main():
    numbers = get_numbers()

    print(f"Sorted list: {numbers}")

    target = get_target()

    index = binary_search(numbers, target)

    if index != -1:
        print(f"{target} was found at index {index}.")
    else:
        print(f"{target} was not found in the list.")


if __name__ == "__main__":
    main()