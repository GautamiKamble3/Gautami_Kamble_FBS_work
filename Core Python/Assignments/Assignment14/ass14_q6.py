# Write a Python program to find the two numbers whose product is
# maximum among all the pairs in a given list of numbers. Use the
# Python set.

numbers = [70, 5, 9, 10, 8]

pairs = set()

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        pairs.add((numbers[i], numbers[j]))

max_product = 0
max_pair = None

for a, b in pairs:
    product = a * b

    if product > max_product:
        max_product = product
        max_pair = (a, b)

print("Pair:", max_pair)
print("Maximum product:", max_product)
