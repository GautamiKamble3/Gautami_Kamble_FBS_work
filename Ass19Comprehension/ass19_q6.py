# comprehension (transforming)
# 6. Use a dictionary comprehension to count the length of each word
# in a sentence

s = input('Enter string to find length of each word: ')

words = {ch: len(ch) for ch in s.split()}

print(words)
