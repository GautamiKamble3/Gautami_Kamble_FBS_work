# Write a program to print all numbers which are divisible by m and n in the list.

l1 = [7, 8, 9, 10, 11, 12, 13, 14, 15]
l2 = []

m = 2
n = 7

for ind in range(len(l1)):
        if(l1[ind] % m == 0 and l1[ind] % n == 0):
            l2 += [l1[ind]]
print(l2)
