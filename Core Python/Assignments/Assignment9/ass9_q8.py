# 8. Write a program to check whether a number is prime or not using recursion.

def primeCal(n):
    for num in range(n):
        if (num > 1):
            for i in range(2, num):
                if num%i == 0:
                    break
            else:
                return True
def checkPrime(n):
    res = primeCal(n)
    if(res == True):
        print(f'{n} is prime number.')
    else:
        print(f'{n} is not a prime number.')

n = int(input('Enter number to check: '))
checkPrime(n)
