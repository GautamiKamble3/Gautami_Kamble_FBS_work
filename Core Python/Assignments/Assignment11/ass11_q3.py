# Python Program to Sort the List According to the Second Element in Sublist

def bubbleSort(li):
    size = len(li)
    for i in range(1, size):
        for j in range(0, size - i):
            if li[j][1] > li[j+1][1]:
                li[j], li[j+1] = li[j+1], li[j]

li = [[1, 5], [3, 2], [7, 9], [4, 1]]
print('List Before Sorting: ', li)
bubbleSort(li)
print('List After Sorting: ', li)
