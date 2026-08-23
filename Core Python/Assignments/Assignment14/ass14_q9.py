# Write a Python program to find all the unique combinations of 3
# numbers from a given list of numbers, adding up to a target number.

numbers = [2, 4, 6, 8, 10, 12]
target = 18

num_set = set(numbers)
combinations = set()

for a in num_set:
    for b in num_set:
        for c in num_set:
            if a < b < c and a + b + c == target:
                combinations.add((a, b, c))

print("Unique combinations:", combinations)
