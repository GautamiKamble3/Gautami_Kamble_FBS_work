# WAP to check if a given number is prime number or not. 

start = int(input('Enter the starting number: '))
end = int(input('Enter the ending number: '))

print(f'The prime numbers between {start} and {end} are: ')

for num in range(start, end):
    if num>1:
        for i in range(2, num):
            if num%i == 0:
                break
        else:
            print(num)
    else:
        print('Number is not prime nor composite')
