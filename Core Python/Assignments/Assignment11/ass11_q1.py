# Python Program to Put Even and Odd elements of a List into two Different Lists

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = []
l3 = []

for ind in range(len(l1)):
    if(l1[ind] % 2 == 0):
        l2 += [l1[ind]]
    else:
        l3 += [l1[ind]]

print('List of even elements : ',l2)
print('List of odd elements : ', l3)
