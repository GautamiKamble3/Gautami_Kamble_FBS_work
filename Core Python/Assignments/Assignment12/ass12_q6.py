# Python Program to Take in a String and Replace Every Blank Space with Hyphen

st = input('Enter string: ')

for ch in st:
    if(ch == ' '):
        print('-', end='')
    else:
        print(ch, end='')
