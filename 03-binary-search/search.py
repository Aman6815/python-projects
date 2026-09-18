def linear_search(numbers, target):
    for index in range(len(numbers)):
        if numbers[index] == target:
            return index

    return -1


def binary_search(numbers, target):
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