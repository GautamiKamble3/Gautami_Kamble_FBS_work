# Python Program to Form a New String where the First Character and
# the Last Character have been Exchanged

str1 = input('Enter string: ')

if len(str1) < 2:
    str2 = str1
else:
    str2 = str1[-1]  # start with last character
    for i in range(1, len(str1) - 1):
        str2 += str1[i]  # add middle characters
    str2 += str1[0]  # add first character at the end

print(str2)   
