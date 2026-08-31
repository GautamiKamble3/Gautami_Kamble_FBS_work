# Python Program to Find the Union of two Lists without
# using set concept.


list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

list3 = list1 + list2

union = []

for i in list3:
    if i not in union:
        union.append(i)

print(union)
