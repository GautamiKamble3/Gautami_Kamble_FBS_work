# 5. Python Program to Count the Number of Vowels in a String

s = input('Enter string: ')
count = 0

for ch in s:  
    if ch in 'aeiouAEIOU':  #iterate over characters
        count += 1

print(f'Vowels in the string are: {count}')
