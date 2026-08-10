# 1. Write a program to find sum of all elements of list

li = [10, 20, 30, 50, 70]
sum = 0
for ind in range(0, len(li)):
    if(ind >= 0):
        sum += li[ind]
print(f'Sum of elements of list is: {sum}')

