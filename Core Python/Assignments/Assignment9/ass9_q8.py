# 8. Write a program to check whether a number is prime or not using recursion.

def isDivisible(n, i):
    if i * i > n:
        return False
    if n % i == 0:
        return True
    return isDivisible(n, i + 1)

def primeCal(n):
    if n <= 1:
        return False
    return not isDivisible(n, 2)

def checkPrime(n):
    res = primeCal(n)
    if res == True:
        print(f'{n} is prime number.')
    else:
        print(f'{n} is not a prime number.')

n = int(input('Enter number to check: '))
checkPrime(n)
