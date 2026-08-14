# Python Program to Take in Two Strings and Display the Larger String
# without Using Built-in Functions

str1 = input('Enter string 1: ')
str2 = input('Enter string 2: ')

count1 = 0
for ind1 in str1:
    count1 += 1

count2 = 0
for ind2 in str2:
    count2 += 1

if count1 > count2:
    print("The larger string is:", str1)
elif count2 > count1:
    print("The larger string is:", str2)
else:
    print("Both strings are of equal length.")
    