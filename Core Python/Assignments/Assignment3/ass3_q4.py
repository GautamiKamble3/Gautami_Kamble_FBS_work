# Write a program to input all sides of a triangle and check whether triangle is valid or not.

# A triangle is valid if the sum of any two sides is greater than the third side.

a=int(input('Enter side first of Triangle:'))
b=int(input('Enter side second of Triangle:'))
c=int(input('Enter side third of Triangle:'))

if(a+b>c and b+c>a and c+a>b):
    print('Triangle is Valid')
else:
    print('Triangle is Invalid')
