# 13. Python Program to count number of digits and letters in a string.

str = input('Enter a string: ')
count1 = 0
count2 = 0

for ch in str:
    if ch.isdigit():
        count1 += 1
    elif ch.isalpha():
        count2 += 1

print('Number of digits:', count1)
print('Number of letters:', count2)
