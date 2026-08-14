# 3. Python Program to Detect if Two Strings are Anagrams

a = 'listen'
b = 'silent'

if len(a) != len(b):
    print('Not Anagram')
else:
    is_anagram = True
    for ch in a:
        counta = 0
        countb = 0
        for i in a:
            if ch == i:
                counta += 1
        for j in b:
            if ch == j:
                countb += 1
        if counta != countb:
            is_anagram = False
            break

    if is_anagram:
        print('Strings are Anagrams')
    else:
        print('Strings are not Anagrams')