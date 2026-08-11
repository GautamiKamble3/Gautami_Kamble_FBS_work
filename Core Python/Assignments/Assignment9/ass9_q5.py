# 5. Write a program to find factorial using recursion.

def fact_total(n):
    if n == 0 or n == 1:
        return 1
    return n * fact_total(n - 1)

def factorial(n):
    res = fact_total(n)
    print(f'Factorial of number is: {res}')

n = int(input('Enter number: '))
factorial(n)
