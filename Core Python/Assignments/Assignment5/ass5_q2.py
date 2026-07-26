#  Enter number of students from user. For those many students accept marks of 5 subject marks from user
# and calculate percentage. Display all percentage and average percentage of students.

n = int(input('Enter total number of students: '))

total_per = 0

for i in range(1, n+1):
    print(f'Student {i}: ')

    sub1 = int(input('Enter marks of subject 1: '))
    sub2 = int(input('Enter marks of subject 2: '))
    sub3 = int(input('Enter marks of subject 3: '))
    sub4 = int(input('Enter marks of subject 4: '))
    sub5 = int(input('Enter marks of subject 5: '))

    total_marks = sub1 + sub2 + sub3 + sub4 + sub5

    percentage = (total_marks/500) * 100

    print(f'Percentage of {i} student is : {percentage}')

    total_per = total_per + percentage

average = total_per/n

print(f'Average percentage of all students are : {average}')

