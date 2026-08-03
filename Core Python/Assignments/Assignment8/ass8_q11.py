# WAP to check if a given number is Armstrong number or not. For each task create separate functions.

def count_digits(num):
    return len(str(num))

def armstrong(num):
    count = count_digits(num)
    temp = num
    total = 0

    while num > 0:
        d = num % 10
        total = total + (d ** count)
        num = num // 10

    if total == temp:
        print("Number is Armstrong")
    else:
        print("Number is not Armstrong")

num = int(input("Enter number: "))
armstrong(num)
