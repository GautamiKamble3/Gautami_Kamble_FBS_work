# 1. Write a program to find sum of following series using recursive functions:
# i. 1! + 2! + 3! + 4! +….. + n!
#  Note : For fact and sum two recursive functions

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def sumFactorial(n):
    if n == 1:
        return factorial(1)
    return factorial(n) + sumFactorial(n - 1)

num = int(input('Enter nth number: '))
print(f'Sum of factorial series is : {sumFactorial(num)}')
