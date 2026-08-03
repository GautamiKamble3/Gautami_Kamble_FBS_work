# Sum of all prime numbers between 1 to n

def prime_sum(n):
    sum = 0
    for num in range(2, n+1):
        for i in range(2, num):
            if num%i == 0:
                break
        else:
            sum += num

    return sum

n = int(input('Enter number n: '))
res = prime_sum(n)
print(f'Sum of all prime numbers between 1 to {n} is : {res}')
