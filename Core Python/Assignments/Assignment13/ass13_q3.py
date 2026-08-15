# 3. Python Program to Check if a Given Key Exists in a Dictionary or Not

dic = {'1': 'one', '2': 'two', '3': 'three', '4': 'fouth', '5': 'fifth'}

search = input('Enter key to search in dictionary : ')

for key in dic:
    if search == key:
        print(f'{key} exists in the dictionary.')
        break
else:
    print('Key does not exists in the dictionary.')
