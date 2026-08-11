# 3. Write a program to reverse a given number using recursive function.

def reverse(n, rev=0):
    if n == 0:
        return rev
    dig = n % 10
    return reverse(n // 10, rev * 10 + dig)

def checkReverse(n):
    res = reverse(n)
    print(f'Reverse of number is : {res}')

n = int(input('Enter number to reverse: '))
checkReverse(n)
