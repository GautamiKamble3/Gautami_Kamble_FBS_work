# 3. Write a Python program to find all the unique words and count the
# frequency of occurrence from a given list of strings. Use Python set
# data type.


def word_freq(strings_list):
    words = " ".join(strings_list).lower().split()
    unique_words = set(words)
    freq = {word: words.count(word) for word in unique_words}
    return unique_words, freq


str_li = ["red blue green", "blue yellow", "red red blue"]
unique_words, freq = word_freq(str_li)

print("Unique words:", unique_words)
print("Frequencies:", freq)
