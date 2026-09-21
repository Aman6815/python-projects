def linear_search(numbers, target):
    for index, number in enumerate(numbers):
        if number == target:
            return index

    return -1


def is_sorted(numbers):
    return all(
        numbers[index] <= numbers[index + 1]
        for index in range(len(numbers) - 1)
    )


def binary_search(numbers, target):
    if not is_sorted(numbers):
        raise ValueError("Binary search requires a sorted list.")

    low = 0
    high = len(numbers) - 1

    while low <= high:
        middle = (low + high) // 2

        if numbers[middle] == target:
            return middle

        if target < numbers[middle]:
            high = middle - 1
        else:
            low = middle + 1

    return -1