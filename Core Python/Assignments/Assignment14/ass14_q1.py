# 1. Write a Python program to find elements in a given set that are not in another set.

s1 = {4, 9, 16, 25, 36}
s2 = {16, 36, 4}

for ele1 in s1:
    for ele2 in s2:
        if ele1 == ele2:
            break
    else:
        print(ele1)
        