# 1. Develop a simple calculator program that performs basic arithmetic operations (+,
# -, *, /) on two numbers provided by the user. The program should ask the user for
# the numbers and the operator. However, the program should handle the following
# exceptions:
# a. Invalid Number: If the user enters a number that is not valid, catch the
# exception and display an error message.
# b. Invalid Operator: If the user enters an operator other than "+", "-", "*", or
# "/", catch the exception and display an error message.
# c. Division by Zero: If the user tries to divide by zero, catch the exception and
# display an error message.
# Write a program that performs the requested arithmetic operation and
# handles the exceptions as described above.
try:
    num1 = int(input('Enter number 1: '))
    num2 = int(input('Enter number 2: '))

except ValueError:
    print('Invalid number..!')
    exit()

operator = input('Enter your operator to perform calculations(+ - * /): ')

try:
    if operator == '+':
        print(f'Addition is : {num1 + num2}')

    elif operator == '-':
        print(f'Subtraction is : {num1 - num2}')

    elif operator == '*':
        print(f'Multiplication is : {num1 * num2}')

    elif operator == '/':
        print(f'Division is : {num1 / num2}')

    else:
        raise ValueError('Invalid Operator')

except ValueError as e:
    print(e)

except ZeroDivisionError:
    print('Division by zero not allowed')

