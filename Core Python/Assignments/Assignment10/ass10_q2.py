# 2. Write a program to find maximum and minimum element in a list.

li = [42, 53, 62, 7, 98, 177, 80, 100]

max = li[0]
for ind in range(1, len(li)):
    if(li[ind] > max):
        max = li[ind]
print(f'Maximum elememt from the list is : {max}')

min = li[0]
for ind in range(1, len(li)):
    if(li[ind] < min):
        min = li[ind]
print(f'Minimum element from the list is : {min}')
