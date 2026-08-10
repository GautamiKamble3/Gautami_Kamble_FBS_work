# 10. Write a program to remove all occurrences of a given element in the list.

l1 = [10, 20, 30, 10, 40, 50, 10, 20]
l2 = []

for i in range(len(l1)):
    count = 0
    for j in range(len(l1)):
        if(l1[i] == l1[j]):
            count += 1

    if(count == 1):
        l2 += [l1[i]]
print(l2)
