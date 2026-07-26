# WAP to print Armstrong number within a given range

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for no in range(start, end + 1):

    count = len(str(no))
    temp = no
    total = 0

    while no > 0:
        d = no % 10
        total = total + (d ** count)
        no = no // 10

    if total == temp:
        print(temp)
        