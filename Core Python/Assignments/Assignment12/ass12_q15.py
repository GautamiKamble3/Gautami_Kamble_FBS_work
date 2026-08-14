# 15. Python Program to find larger string without using built-in functions.

str1 = input('Enter string 1: ')
str2 = input('Enter string 2: ')

count1 = 0
for ch in str1:
    count1 += 1

count2 = 0
for ch in str2:
    count2 += 1

if count1 > count2:
    print('String 1 is larger:', str1)
elif count2 > count1:
    print('String 2 is larger:', str2)
else:
    print('Both strings are of equal length.')
