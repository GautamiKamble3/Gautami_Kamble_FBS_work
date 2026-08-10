# 6. Write a program to remove duplicates from the list.

l1 = [7, 14, 21, 28, 35, 7, 21]
l2 = []

for i in range(len(l1)):
    ele = False
    for j in range(len(l2)):
        if(l1[i] == l2[j]):
            ele = 1
    if(ele == 0):
        l2 += [l1[i]]
print(l2)
