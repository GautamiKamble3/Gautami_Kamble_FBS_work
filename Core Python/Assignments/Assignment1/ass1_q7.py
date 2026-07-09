# Program to Find the Roots of a Quadratic Equation
# Divide and merge rule
#ax2 + bx + c = 0

a = int(input("Enter coefficient of a : "))
b = int(input("Enter coefficient of b : "))
c = int(input("Enter coefficient of c : "))

d = (b**2) - (4*a*c)

root1 = (-b + d**0.5) / (2 * a)
root2 = (-b - d**0.5) / (2 * a)

print("Roots of quadratic equations are : ", root1 ,root2)

