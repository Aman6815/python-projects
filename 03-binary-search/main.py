from search import binary_search


numbers = [3, 7, 12, 18, 25, 31, 42, 56, 68, 79]


def main():
    try:
        target = int(input("Enter a number to search for: "))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return

    index = binary_search(numbers, target)

    if index != -1:
        print(f"{target} was found at index {index}.")
    else:
        print(f"{target} was not found in the list.")


if __name__ == "__main__":
    main()