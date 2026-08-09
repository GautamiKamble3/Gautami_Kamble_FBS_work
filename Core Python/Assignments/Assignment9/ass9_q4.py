# 4. Write a program to find sum of n numbers using recursion.

def sumCalculation(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum

def totalSum(n):
    res = sumCalculation(n)
    print(f'Sum of numbers is : {res}')

n = int(input('Enter nth number: '))
totalSum(n)
