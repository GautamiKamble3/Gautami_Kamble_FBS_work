# WAP to check if given number Strong Number

num=int(input('Enter a number to check strong number or not:'))

temp=num
sum=0

while(temp>0):
    d=temp%10
    temp=temp//10
    fact=1
    for i in range(1,d+1):
        fact=fact*i
    sum=sum+fact

if(sum==num):
    print(f'{num} is a strong number')
else:
    print(f'{num} is not a strong number')
    