numbers = [3, 7, 12, 18, 25, 31, 42, 56, 68, 79]

target = int(input("Enter a number to search for: "))

found = False

for number in numbers:
    if number == target:
        found = True
        break

if found:
    print(f"{target} was found in the list.")
else:
    print(f"{target} was not found in the list.")