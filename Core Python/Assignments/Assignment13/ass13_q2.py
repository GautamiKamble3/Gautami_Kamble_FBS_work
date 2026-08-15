# Python Program to Concatenate Two Dictionaries Into One

d1 = {'id': 102, 'name': 'Kunal', 'sal': '70000', 'dept': 'IT'}
d2 = {'addr' : 'pune', 'gender' : 'male'}

d3 = {}

for key in d1:
    d3[key] = d1[key]

for key in d2:
    d3[key] = d2[key]

print(d3)
