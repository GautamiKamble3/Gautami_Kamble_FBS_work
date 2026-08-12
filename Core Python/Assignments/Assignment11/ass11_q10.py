# Write a program to print list after removing even numbers.

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = []

for ind in range(0, len(l1)):
    if(l1[ind] % 2 != 0):
        l2 += [l1[ind]]

print('List After Removing Even Numbers: ', l2)
