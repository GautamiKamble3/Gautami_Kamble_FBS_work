# 5. Accept a number from user and check if this element is present in the list or not.
#    Also tell how many times it is present in the list.

num = int(input('Enter number to check in list: '))
li = [10, 20, 30, 10, 70, 50, 20, 20]

count = 0
for ind in range(len(li)):
    if(li[ind] == num):
        count += 1

if count > 0:
    print(f'{num} is present in the list and Count is  :  {count}')
else:
    print(f'{num} is not present in the list.')
