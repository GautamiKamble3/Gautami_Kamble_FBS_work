# Find the sum of three-digit number.

#temp = num      #to store original number

num = int(input("Enter three digit number: "))

d1 = num % 10
num = num // 10

d2 = num % 10
num = num // 10

d3 = num % 10
num = num // 10

sum = d1 + d2 + d3

print(f'Sum of Three Digit Number is {sum}')