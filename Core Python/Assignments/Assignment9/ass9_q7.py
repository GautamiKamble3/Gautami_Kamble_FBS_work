# 7. Write a program to find sum of digits using recursion.

def calculationSum(n):
    if n == 0:
        return 0
    dig = n % 10
    return dig + calculationSum(n // 10)

def sumDigits(n):
    res = calculationSum(n)
    print(f'Sum of digits is : {res}')

n = int(input('Enter digit to calculate sum: '))
sumDigits(n)
