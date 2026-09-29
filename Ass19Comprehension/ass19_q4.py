# 4. Remove all of the vowels in a string

s = input('Enter string to remove vowels: ')

# output in list
result = [ch for ch in s if ch not in 'aeiouAEIOU']
print(result)

print()

# output as a normal string
result = ''.join([ch for ch in s if ch not in 'aeiouAEIOU'])
print(result)
