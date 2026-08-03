# Write a program to find sum of digits of a number

def sum_digits(n):
    
    total = 0
    while(n > 0):
        d = n % 10
        n = n // 10
        total += d
    return total

n = int(input('Enter number n: '))
res = sum_digits(n)
print(f'Sum of Digits of number {n} is {res}')
