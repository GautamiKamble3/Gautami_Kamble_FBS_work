# 3. Write a generator function that mimics the behavior of the built-in
# range() function. The generator should take start, stop, and step
# arguments and yield numbers within the specified range.

def genRange(start, stop, step):

    while start < stop:
        yield start
        start = start + step


g = genRange(1, 10, 2)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
