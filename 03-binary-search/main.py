import time

from search import binary_search, linear_search


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


def choose_search_algorithm():
    while True:
        print("\nChoose a search algorithm:")
        print("1. Linear Search")
        print("2. Binary Search")

        choice = input("Enter your choice: ")

        if choice == "1":
            return linear_search

        if choice == "2":
            return binary_search

        print("Invalid choice. Please enter 1 or 2.")


def measure_search_time(search_algorithm, numbers, target):
    start_time = time.perf_counter()
    index = search_algorithm(numbers, target)
    end_time = time.perf_counter()

    elapsed_time = end_time - start_time

    return index, elapsed_time


def main():
    numbers = get_numbers()

    print(f"Sorted list: {numbers}")

    target = get_target()
    search_algorithm = choose_search_algorithm()

    index, elapsed_time = measure_search_time(
        search_algorithm,
        numbers,
        target
    )

    if index != -1:
        print(f"{target} was found at index {index}.")
    else:
        print(f"{target} was not found in the list.")

    print(f"Search time: {elapsed_time:.10f} seconds")


if __name__ == "__main__":
    main()