# 7. Python Program to Remove the Given Key from a Dictionary

dic = {'id': 102, 'name': 'Kunal', 'sal': '70000', 'dept': 'IT'}

n = input('Enter key to remove from the dictionary: ')

new_dic = {}

for key in dic:
    if key != n:
        new_dic[key] = dic[key]

if len(new_dic) < len(dic):
    print('Updated Dictionary:', new_dic)
else:
    print('Key not found in dictionary')

dic = new_dic
