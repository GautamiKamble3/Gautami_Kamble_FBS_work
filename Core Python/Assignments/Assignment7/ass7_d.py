# pattern d

n = 5

for i in range(1, n + 1):
    for j in range(1, n - i + 1):
        print(" ", end=" ")

    # Increasing numbers
    num = i
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1

    # Decreasing numbers
    num -= 2
    for j in range(1, i):
        print(num, end=" ")
        num -= 1

    print()