# Python Program to Find the Second Largest Number in a List Using Bubble Sort 

def bubbleSort(li):
    max = li[0]
    sec_max = li[0]

    for ind in range(0, len(li)):
        if(li[ind] > max):
            sec_max = max
            max = li[ind]

        elif(li[ind] > sec_max and li[ind] != max):
            sec_max = li[ind]

    return sec_max

li = [42, 53, 62, 127, 7, 98, 177, 80, 100]
res = bubbleSort(li)
print(f'Second Largest element in the list is : {res}')
