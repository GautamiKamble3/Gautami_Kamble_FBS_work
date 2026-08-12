# Python Program to Find the Intersection of Two Lists

l1 = [1, 2, 3, 4, 5,7]
l2 = [6, 7,3, 8, 9, 10,2]
l3 = []

for i in range(0, len(l1)):
    for j in range(0, len(l2)):
        if(l1[i] == l2[j]):
            l3 += [l1[i]]


print("Intersection of Two Lists are : ", l3)    

