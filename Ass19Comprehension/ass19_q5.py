# comprehension(filtering)
# 5. Find all of the words in a string that are less than 5 letters

s = input('Enter string to find words: ')

words = [ch for ch in s.split() if(len(ch) < 5)]

print(f'Words in string less than 5 letters : {words}')
