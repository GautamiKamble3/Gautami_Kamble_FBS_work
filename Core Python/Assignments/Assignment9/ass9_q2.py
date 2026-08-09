# 2. Write a program to check if given number is Armstrong or not using recursive function.

def countDig(n):
    return len(str(n))

def checkArmstrong(n):
    cnt = countDig(n)
    temp = n
    sum = 0

    while (n > 0):
        dig = n % 10
        sum = sum + (dig ** cnt)
        n = n // 10

    if(sum == temp):
        print('Number is Armstrong number')
    else:
        print('Number is not Armstrong number')

n = int(input('Enter number to check: '))
checkArmstrong(n)
