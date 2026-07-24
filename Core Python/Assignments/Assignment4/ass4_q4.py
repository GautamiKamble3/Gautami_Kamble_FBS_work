#  WAP to print factorial of a number . 

n = int(input('Enter value of n: '))

fact = 1
for i in range(1, n+1):
    fact = fact * i
print(f'Factorial of {n} numbers is : {fact}')
