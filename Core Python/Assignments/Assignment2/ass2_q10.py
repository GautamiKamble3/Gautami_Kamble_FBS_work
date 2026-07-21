# Write a program to reverse three-digit number.
# take 3 digit number to reverse

digit = int(input('Enter three digit number: '))

digit1 = digit % 10
num = digit // 10

digit2 = num % 10
num = num // 10

digit3 = num % 10
num = num // 10

rev = digit1 * 100 + digit2 * 10 + digit3 
print(f'Reverse three digit number is : {rev}')
