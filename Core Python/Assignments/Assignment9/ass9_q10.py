# 10. Write a program to reverse a number using recursion.

def calculateReverse(n):
    rev = 0
    while(n > 0):
        dig = n % 10
        n = n // 10
        rev = rev * 10 + dig
    return rev

def reversedNum(n):
    res = calculateReverse(n)
    print(f'Reverse of number is : {res}')

n = int(input('Enter number to reverse: '))
reversedNum(n)
