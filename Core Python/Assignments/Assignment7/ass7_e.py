# pattern e

n = 5

for i in range(1, n + 1):
    # Print leading spaces
    for j in range(1, n - i + 1):
        print(" ", end=" ")

    if i == 1:
        print(1)
    elif i == n:
        # Print last row
        for j in range(1, n + 1):
            if j == n:
                print(j, end="")
            else:
                print(j, end=" ")
            print(" ", end=" ")

        print()

    else:
        # Print left side
        print(1, end=" ")
        # Print middle spaces
        for j in range(1, 2 * i - 2):
            print(" ", end=" ")

        # Print right side
        print(i)
