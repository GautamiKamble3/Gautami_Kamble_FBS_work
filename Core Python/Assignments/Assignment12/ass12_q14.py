# 14. Python Program to count the occurrences of each word in a string.

text = input('Enter your string: ')

word_list = text.split()
word_count = {}

for word in word_list:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for word, count in word_count.items():
    print(word, ':', count)
