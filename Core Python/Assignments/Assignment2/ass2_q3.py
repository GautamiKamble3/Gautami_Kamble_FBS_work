# Convert distant given in feet and inches into meter and centimeter.

feet = float(input("Enter feet: "))
inches = float(input("Enter inches: "))

total_inches = (feet * 12) + inches

cm = total_inches * 2.54
m = cm / 100

print(f'Distant in meters {m}')
print(f'Distant in centimeter {cm}')