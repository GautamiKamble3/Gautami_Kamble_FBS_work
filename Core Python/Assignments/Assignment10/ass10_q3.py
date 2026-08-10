# 3. Write a program to find the second largest element in the list.

li = [42, 53, 62, 7, 98, 177, 80, 100]

max = li[0]
sec_max = li[0]

for ind in range(0, len(li)):
    if(li[ind] > max):
        sec_max = max
        max = li[ind]

    elif(li[ind] > sec_max and li[ind] != max):
        sec_max = li[ind]
print(f'Second Largest element in the list is : {sec_max}')
