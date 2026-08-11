# 10. Write a program to reverse a number using recursion.

def calculateReverse(n, rev=0):
    if n == 0:
        return rev
    dig = n % 10
    return calculateReverse(n // 10, rev * 10 + dig)

def reversedNum(n):
    res = calculateReverse(n)
    print(f'Reverse of number is : {res}')

n = int(input('Enter number to reverse: '))
reversedNum(n)
