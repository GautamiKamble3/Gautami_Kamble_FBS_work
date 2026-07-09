# Write a Program to input two angles from user and find third angle of the triangle.

angle1 = int(input("Enter angle 1: "))
angle2 = int(input("Enter angle 2: "))

angle3 = 180 - (angle1 + angle2)

print("Third angle of a triangle is:  ", angle3)