# 6. Python Program to Multiply All the Items in a Dictionary

dic = {'1': 10  , '2' : 20 , '3' : 30}

mul = 1
for key in dic:
    mul = mul * dic[key]
print(f'Multiplication of all the Items in a Dictionary : {mul}')
