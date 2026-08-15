# 5. Python Program to Sum All the Items in a Dictionary

dic = {'1': 100  , '2' : 200 , '3' : 300}

sum = 0
for key in dic:
    sum = sum + dic[key]
print(f'Sum of all the items in a Dictionary : {sum}')
