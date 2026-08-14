# Python Program to Calculate the Length of a String Without Using a Library Function

st = input('Enter string: ')

count = 0
for ch in st:
    if(ch == ch):
        count += 1

print(count)
