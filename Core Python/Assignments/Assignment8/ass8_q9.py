# Write a program to check if entered number is a palindrome or not.

def palindrome(n):

    rev = 0
    temp = n

    while(temp > 0):
        d = temp % 10
        temp = temp // 10
        rev = rev*10+d
        
    if(n == rev):
        print(f'{n} is palindrome number.')
    else:
        print(f'{n} is not palindrome number. ')    

n = int(input('Enter number to check: '))
palindrome(n)
