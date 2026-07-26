# Write a program to solve the following series :

# a. 1! + 2! + 3! + 4! + .....n!
n=int(input('Enter number:'))
for no in range(1,n+1):
    fact=1
    sum=0
    for i in range(1,no+1):
        fact=fact*i
        sum=sum+fact
        
print(f'sum of 1 to {n} factorial')
print(f'sum of series= {sum}')

# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
N=int(input('Enter the base value:'))
sum=0
for no in range(1,N+1):
    sum=sum+N**no
print('sum of series= ',sum)


# # b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
N=int(input('Enter the base value:'))
endnum=int(input('Enter the ending power:'))
sum=0
for no in range(1,endnum+1):
    sum=sum+N**no
print('sum of series=',sum)

# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
endnum=int(input('Enter the ending value:'))
sum=0
a=1
r=2
for i in range(1,endnum+1):
    sum+=a*(r**i)
print('sum',sum)


# d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
a=int(input('Enter the base value:'))
endnum=int(input('Enter the ending power:'))
sum=0
for no in range(1,endnum+1):
    sum=sum+(a**no)/no
print('sum of series=',sum)

# d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
a=int(input('Enter the base value:'))
sum=0
for no in range(1,a+1):
    sum=sum+(a**no)/no
print('sum of series=',sum)


# e. x - x2/3 + x3/5 - x4/7 + .... to n terms
x=int(input('Enter the number:'))
n=int(input('Enter the ending value:'))
deno=1
sign=1
sum=0
for i in range(1,n+1):
    sum+=sign*((x**i)/deno)
    deno+=2
    sign*=-1
print(f'sum of series= {sum}')
