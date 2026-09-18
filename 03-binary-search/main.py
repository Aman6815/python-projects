def linear_search(numbers, target):
    for number in numbers:
        if number == target:
            return True

    return False


def binary_search(numbers, target):
    low = 0
    high = len(numbers) - 1

    while low <= high:
        middle = (low + high) // 2

        if numbers[middle] == target:
            return True

        if target < numbers[middle]:
            high = middle - 1
        else:
            low = middle + 1

    return False


numbers = [3, 7, 12, 18, 25, 31, 42, 56, 68, 79]

target = int(input("Enter a number to search for: "))

found = binary_search(numbers, target)

if found:
    print(f"{target} was found in the list.")
else:
    print(f"{target} was not found in the list.")