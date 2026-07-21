# Write a program to swap two numbers without using third variable.

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print(f'Swap Numbers are num1 is {num1} and num2 is {num2}')
