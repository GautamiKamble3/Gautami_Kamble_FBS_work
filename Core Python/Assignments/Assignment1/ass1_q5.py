# Write a program to enter P, T, R and calculate Compound Interest.

P = int(input("Enter principal amount: "))
R = int(input("Enter rate of interest: "))
T = int(input("Enter time in years: "))

amount = P * (1 + R / 100) ** T

CI = amount - P

print("Compound Interest is : ", CI)