# 4. Write a program to find sum of n numbers using recursion.

def sumCalculation(n):
    if n == 0:
        return 0
    return n + sumCalculation(n - 1)

def totalSum(n):
    res = sumCalculation(n)
    print(f'Sum of numbers is : {res}')

n = int(input('Enter nth number: '))
totalSum(n)

