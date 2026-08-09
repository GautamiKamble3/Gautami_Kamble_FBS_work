# 3. Write a program to reverse a given number using recursive function.

def reverse(n):
    rev = 0
    while(n > 0):
        dig = n % 10
        n = n // 10
        rev = rev * 10 + dig
    return rev

def checkReverse(n):

    res = reverse(n)
    print(f'Reverse of number is : {res}')

n = int(input('Enter number to reverse: '))
checkReverse(n)
