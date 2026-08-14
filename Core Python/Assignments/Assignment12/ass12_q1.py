# 1. Python Program to Replace all Occurrences of ‘a’ with $ in a String

s = input('Enter string: ')

for ch in s:
    if(ch == 'a'):
        print('$', end='')
    else:
        print(ch, end='')
