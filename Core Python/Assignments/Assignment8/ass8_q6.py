# Write a program to find print the following Fibonacci series using
# functions:
#  1 1 2 3 5 8 n terms

def fibonacci_series(n):
    a = 1
    b = 1
    for i in range(n):
        print(a)
        c = a + b
        a = b
        b = c

n = int(input('Enter number n: '))
fibonacci_series(n)

