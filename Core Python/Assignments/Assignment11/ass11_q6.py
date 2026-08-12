# 6. Python Program to Find the Union of two Lists

l1 = [1, 2, 3, 4, 5, 7]
l2 = [6, 7, 3, 8, 9, 10, 2]
l3 = []

for i in range(0, len(l1)):
    l3 += [l1[i]]

for i in range(0, len(l2)):
    ele = False
    for j in range(0, len(l3)):
        if l2[i] == l3[j]:
            ele = True
    if not ele:
        l3 += [l2[i]]

print("Union of Two Lists are : ", l3)
