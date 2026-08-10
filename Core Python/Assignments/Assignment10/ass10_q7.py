# 7. Write a program to create a new list from existing list which contains cube of each number of list.

li = [1, 2, 3, 4, 5, 6, 7]
l2 = []

for i in range(len(li)):
    l2 = l2 + [li[i] ** 3]

print('New list is :',l2)
