# WAP to check if given number is Perfect Number. 

num = int(input("Enter a number: "))

sum = 0

for i in range(1, num):
    if num % i == 0:
        sum = sum + i

if sum == num:
    print(f'{num} is a Perfect Number')
else:
    print(f'{num} is not Perfect Number')
