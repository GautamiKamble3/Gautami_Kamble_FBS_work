# 4. There is a list with some numbers. Create a new
# dictionary using this list in such a way that key is
# number and value is frequency of occurrence of that
# number in list.
# [1,3,4,1,2,3,6,7,1,2,4]


num = [1,3,4,1,2,3,6,7,1,2,4]
freq = {}

for i in num:
    if i in freq:
        freq[i] = freq[i] + 1
    else:
        freq[i] = 1

print(freq)
