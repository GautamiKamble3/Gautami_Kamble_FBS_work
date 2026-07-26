# Write a program to print first n prime numbers. 

n = int(input("Enter how many prime numbers: "))

count = 0
num = 2

while count < n:

    if(num > 1):
        for i in range(2, num // 2 + 1):
            if(num % i == 0):
                break
        else:
            print(num)
            count = count + 1

    num = num + 1
