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


numbers = [3, 7, 12, 18, 25, 31, 42, 56, 68, 79]

target = int(input("Enter a number to search for: "))

index = binary_search(numbers, target)

if index != -1:
    print(f"{target} was found at index {index}.")
else:
    print(f"{target} was not found in the list.")