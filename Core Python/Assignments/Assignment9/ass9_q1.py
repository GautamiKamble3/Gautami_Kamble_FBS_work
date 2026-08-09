# 1. Write a program to find sum of following series using recursive functions:
# i. 1! + 2! + 3! + 4! +….. + n!
#  Note : For fact and sum two recursive functions

def factorial():
    n = int(input('Enter nth number: '))
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

def sumFactorial():
    sum = 0
    fact = factorial()
    sum += fact 
    print(f'Sum of factorial series is : {sum}')
    
sumFactorial()
