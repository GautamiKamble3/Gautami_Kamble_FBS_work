# 1. We want to generate Fibonacci numbers up to a certain limit.
# Instead of computing and storing the entire sequence in memory,
# create generator to yield Fibonacci numbers one by one,
# conserving memory and allowing for easy iteration.

def genFibonacci(limit):
    a = 0
    b = 1
    for i in range(limit):
        yield a
        c = a + b
        a = b
        b = c

g = genFibonacci(10)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
