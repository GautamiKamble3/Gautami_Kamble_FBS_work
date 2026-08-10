# 8. Write a program to create a duplicate of an existing list. It should not point to same list.

li = [1, 2, 3, 4, 5]
l2 = []

for i in range(len(li)):
    l2 = l2 + [li[i]]

print("Original list:", li)
print("Duplicate list:", l2)

# Proof they are different objects
li[0] = 100
print("\nAfter modifying li[0]:")
print("Original list:", li)
print("Duplicate list:", l2)
