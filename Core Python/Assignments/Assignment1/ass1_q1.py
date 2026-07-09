# Write a program to calculate the percentage of student based on marks of any 5 subjects.

sub1 = int(input("Enter marks obtained in subject 1: "))
sub2 = int(input("Enter marks obtained in subject 2: "))
sub3 = int(input("Enter marks obtained in subject 3: "))
sub4 = int(input("Enter marks obtained in subject 4: "))
sub5 = int(input("Enter marks obtained in subject 5: "))

total_marks = sub1 + sub2 + sub3 + sub4 + sub5 

result = (total_marks/500)*100

print(f'Percentage obtained is : ', result)