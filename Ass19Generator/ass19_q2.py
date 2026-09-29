# 2. Implement a generator function that yields palindrome numbers.
# Palindromes are numbers that read the same backward as forward
# (e.g., 121, 1331). Generate palindromes lazily and infinitely.

def genPalindrome(num):

    while True:
        temp = num
        rev = 0

        while temp > 0:
            dig = temp % 10
            rev = rev * 10 + dig
            temp = temp // 10

        if rev == num:
            yield num

        num += 1

g = genPalindrome(121)

for i in range(5):
    print(next(g))
