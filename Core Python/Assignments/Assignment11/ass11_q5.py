# Python Program to Sort a List According to the Length of the Elements within the list.

def selectionSort(li):
    size = len(li)
    for i in range(0, size - 1):
        min_ind = i
        for j in range(i+1, size):
            if len(li[j]) < len(li[min_ind]):
                min_ind = j
        li[i], li[min_ind] = li[min_ind], li[i]

li = ["banana", "kiwi", "watermelon", "fig", "apple"]
print('Before sorting : ', li)
selectionSort(li)
print('After Sorting : ', li)
