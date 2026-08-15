# Python Program to Generate a Dictionary that Contains Numbers (between 1
# and n) in the Form (x,x*x).

n = int(input('Enter nth number: '))
d = {}

for key in range(1, n+1):
    d[key] = key*key
print(d)
