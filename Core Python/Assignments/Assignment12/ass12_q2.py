# Python Program to Remove the nth Index Character from a Non-Empty String

s = 'Character'
n = 2  # index of character to remove

result = ""
for ind in range(len(s)):
    if ind != n:
        result += s[ind]

print(result)  

