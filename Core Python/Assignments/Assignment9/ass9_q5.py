# 5. Write a program to find factorial using recursion.

def fact_total(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

def factorial(n):
    res = fact_total(n)
    print(f'Factorial of number is: {res}')

n = int(input('Enter number: '))
factorial(n)
