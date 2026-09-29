# comprehension (filtering)
# 3. Count the number of spaces in a string (take input from user)

s = input('Enter string to count spaces: ')

spaces = [ch for ch in s if(ch == ' ')]

print('Number of spaces:', len(spaces))
