#Pattern a

n = 5

# Upper Part
for i in range(1, n + 1):
    for j in range(1, n - i + 1):
        print(" ", end=" ")
    print("*", end=" ")

    if i > 1:
        for j in range(1, 2 * i - 2):
            print(" ", end=" ")
        print("*", end=" ")
    print()

# Lower Part
for i in range(n - 1, 0, -1):
    for j in range(1, n - i + 1):
        print(" ", end=" ")
    print("*", end=" ")

    if i > 1:
        for j in range(1, 2 * i - 2):
            print(" ", end=" ")
        print("*", end=" ")

    print()
    