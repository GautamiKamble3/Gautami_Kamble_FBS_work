# Write a program to find sum of following series using functions :

# a. 1+ 2 + 3 + 4+….. + n
def sum_series(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum
n = int(input('Enter number of sum: '))
res = sum_series(n)
print(f'Sum of 1 to {n} = {res}')
print()

# b. 1!+ 2! + 3! + 4!+….. + n!
def sum_factorial(n):
    fact = 1
    total = 0
    for i in range(1, n + 1):
        fact *= i
        total += fact
    return total
n = int(input('Enter number for factorial: '))
print(f'Sum of Factorial {n} is {sum_factorial(n)}')
print()

# c. 1^1 + 2^2 + 3^3+ …… n^n
# c. 1^1 + 2^2 + 3^3 + ..... + n^n
def sum_power(n):
    total = 0
    for i in range(1, n+1):
        total += i**i
    return total
n = int(input('Enter number for power: '))
res = sum_power(n)
print(f'Sum of 1^1 to {n}^{n} = {res}')
