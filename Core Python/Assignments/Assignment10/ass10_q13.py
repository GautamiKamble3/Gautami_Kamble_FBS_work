# 13 . Write a program to print list after removing even numbers.

l1 = [2, 8, 19, 15, 7, 10, 23]
l2 = []

for ind in range(len(l1)):
    if l1[ind] % 2 != 0:
        l2 += [l1[ind]]

print(l2)   
