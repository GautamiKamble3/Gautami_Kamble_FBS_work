# WAP to calculate area of triangle and rectangle

#Area of Triangle
base = int(input("Enter base of Triangle: "))
height = int(input("Enter height of Triangle: "))

area_tri = ((base * height) / 2)

print(f'Area of Triangle is : {area_tri}')

#Area of Rectangle
length = int(input("Enter Lenght of Rectangle: "))
breadth = int(input("Enter Breadth of Rectangle: "))

area_rect = length * breadth 

print(f'Area of Rectangle is : {area_rect}')