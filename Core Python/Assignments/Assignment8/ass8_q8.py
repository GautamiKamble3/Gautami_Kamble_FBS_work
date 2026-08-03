# Write a program find reverse of a number

def reverse_num(n):

    rev = 0
    while(n > 0):
        d = n % 10
        n = n // 10
        rev = rev *10 + d
    return rev

n = int(input('Enter number : '))
res = reverse_num(n)
print(f'Reverse of number {n} is : {res}')
