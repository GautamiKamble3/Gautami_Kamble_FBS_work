# Write a program to check whether the triangle is equilateral, isosceles or scalene triangle

a=int(input('Enter side first of Triangle:'))
b=int(input('Enter side second of Triangle:'))
c=int(input('Enter side third of Triangle: '))

if(a==b==c):
    print('This is equilateral triangle') 

elif(a == b or b == c or a == c):
    print('This is isosceles triangle')
    
else:
    print('This is scalene triangle') #  (a != b and b != c and a != c)
