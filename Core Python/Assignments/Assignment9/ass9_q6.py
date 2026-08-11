# 6. Write a program to print Fibonacci series using recursion.

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def totalFibonacci(n):
    for i in range(n):
        print(fibonacci(i))

n = int(input('Enter nth number for fibonacci series: '))
totalFibonacci(n)
