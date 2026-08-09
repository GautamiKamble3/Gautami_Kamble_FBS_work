# 7. Write a program to find sum of digits using recursion.

def calculationSum(n):
    sum = 0
    while(n > 0):
        dig = n % 10
        n = n // 10
        sum += dig
    return sum
    
def sumDigits(n):
    res = calculationSum(n)
    print(f'Sum of digits is : {res}')

n = int(input('Enter digit to calculate sum: '))
sumDigits(n)
