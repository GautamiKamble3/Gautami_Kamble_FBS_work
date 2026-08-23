# 2. Write a Python program to remove the intersection of a second set with a first set.

s1 = {45, 65, 82, 18, 7}
s2 = {18, 7, 12}   

result = set()
for ele1 in s1:
    for ele2 in s2:
        if ele1 == ele2:
            break
    else:
        result.add(ele1)

print(result)
