# 11. Python Program to replace every blank space with hyphen in a string.

st = 'Hard Work Will Paid Off'

for ch in st:
    if(ch == ' '):
        print('-', end='')
    else:
        print(ch, end='')
