# 2. Write a program to check if given number is Armstrong or not using recursive function.

def countDig(n):
    return len(str(n))

def sumOfPowers(n, cnt):
    if n == 0:
        return 0
    dig = n % 10
    return (dig ** cnt) + sumOfPowers(n // 10, cnt)

def checkArmstrong(n):
    cnt = countDig(n)
    result = sumOfPowers(n, cnt)

    if result == n:
        print('Number is Armstrong number')
    else:
        print('Number is not Armstrong number')

n = int(input('Enter number to check: '))
checkArmstrong(n)
