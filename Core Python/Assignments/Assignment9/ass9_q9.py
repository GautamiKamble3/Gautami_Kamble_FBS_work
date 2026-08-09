# 9. Write a program to calculate the m to the power n using recursion.

def powerCal(m,n):
    if n == 0:
        return 1
    return  m*powerCal(m,n-1)

m = int(input('Enter base number: '))
n = int(input('Enter power number: '))
res=powerCal(m,n)
print(f'{m}**{n} = {res}')
