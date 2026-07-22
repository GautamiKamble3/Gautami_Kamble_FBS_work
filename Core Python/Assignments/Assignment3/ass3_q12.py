# Write a program to check if given 3 digit number is a palindrome or not.

num = int(input('Enter 3 digit number: '))

temp = num 
rev = 0
while(num > 0):
    d = num % 10
    num = num // 10
    rev = rev * 10 + d
    # print(d)

if(temp == rev):
    print('Number is Palindrome')
else:
    print('Number is Not Palindrome')
