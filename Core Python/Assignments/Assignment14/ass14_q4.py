# Write a Python program that finds all pairs of elements in a list whose
# sum is equal to a given value.

num = [2, 4, 3, 5, 7, 8, 9]
target = 10

pairs = set()

for i in range(len(num)):
    for j in range(i + 1, len(num)):
        if num[i] + num[j] == target:
            pairs.add((num[i], num[j]))

print("Pairs whose sum is", target, ":", pairs)
