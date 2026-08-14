# Python Program to Calculate the Number of Words and the Number of
# Characters Present in a String

st = input('Enter string: ')

word_count = 1  
char_count = 0

for ind in st:
    if ind == ' ':
        word_count += 1
    else:
        char_count += 1

print("Number of words:", word_count)
print("Number of characters:", char_count)
