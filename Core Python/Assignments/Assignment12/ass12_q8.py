# Python Program to Remove the Characters of Odd Index Values in a String

st = input('Enter string: ')

result = ''
index = 0
for ch in st:
    if index % 2 == 0:
        result = result + ch
    index = index + 1

print(result)
