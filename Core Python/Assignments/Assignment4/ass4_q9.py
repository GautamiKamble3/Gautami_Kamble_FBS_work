# WAP to print all numbers in a range divisible by a given number

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

div = int(input('Enter divisible number: '))

print(f'Number divisible by {div} in range {start} to {end} are: ')

for i in range(start, end + 1):
    if i % div == 0:
        print(i)
