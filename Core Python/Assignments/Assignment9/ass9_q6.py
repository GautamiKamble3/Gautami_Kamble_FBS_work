# 6. Write a program to print Fibonacci series using recursion.

def fibonacci(n):
    res = totalFibonacci(n)
    return res

def totalFibonacci(n):
    a = -1
    b = 1
    for i in range(n):
        c = a + b
        print(c)
        a = b 
        b = c

n = int(input('Enter nth number for fibonacci series: '))
fibonacci(n)
