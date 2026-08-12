# Write a program to create three lists of numbers, their squares and cubes

l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = []
l3 = []

for i in range(len(l1)):
    l2 += [l1[i] ** 2]
    l3 += [l1[i] ** 3]

print('List 1 : ', l1)
print('List 2(squares) : ', l2)
print('List 3(cubes) : ', l3)

