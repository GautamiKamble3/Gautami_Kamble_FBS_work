# WAP to calculate total salary of employee based on basic, da=10% of basic,
# ta=12% of basic, hra=15% of basic.

# da = Dearness Allowance
# ta = Travel Allowance (Transport Allowance)
# hra = House Rent Allowance 

basic_sal = int(input("Enter your basic salary: "))

da = basic_sal * (10/100)
ta = basic_sal * (12/100)
hra = basic_sal * (15/100)

total_sal = basic_sal + da + ta + hra

print(f'Total Salary of Employee is: {total_sal}')