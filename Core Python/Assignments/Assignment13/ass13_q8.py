# Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary

string = input('Enter a string: ')

words = string.split()

freq = {}

for word in words:
    if word in freq:
        freq[word] = freq[word] + 1
    else:
        freq[word] = 1

print('Word frequency:', freq)
