# Write a program of having n number of elements in the list and find out even and odd elements in that list
# and then create two separate lists which will have even elements and other will have odd elements. 

n = int(input("Enter number of elements: "))
l1 = []

for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    l1 += [num]

even_list = []
odd_list = []

for ind in range(len(l1)):
    if l1[ind] % 2 == 0:
        even_list += [l1[ind]]
    else:
        odd_list += [l1[ind]]

print('List       : ', l1)
print('Even List  : ', even_list)
print('Odd List   : ', odd_list)
