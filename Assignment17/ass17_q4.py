# 4. Create a class College which has collection of students. Add the
# following methods :
# a. Parameteried constructor for number of students.
# b. AddStudent
# c. GetStudent
# d. RemoveStudent
# e. Override __str__ Method

class Student:
    def __init__(self, sid, sname, sage, sper):
        self.sid = sid
        self.sname = sname
        self.sage = sage
        self.sper = sper
    def getSid(self):
        return self.sid
    def __str__(self):
        return f'ID = {self.sid} | Name = {self.sname} | Age = {self.sage} | Percentage = {self.sper}'


class College:

    def __init__(self, noS):
        self.students = []
        self.noS = noS

    def AddStudent(self, student):
        if len(self.students) < self.noS:
            self.students.append(student)
            print('Student Added')
        else:
            print('College is Full')

    def GetStudent(self, sid):
        for student in self.students:
            if student.getSid() == sid:
                return student
        return None

    def RemoveStudent(self, sid):
        for student in self.students:
            if student.getSid() == sid:
                self.students.remove(student)
                print('Student Removed')
                return
        print('Student Not Found')

    def __str__(self):
        result = ''
        for student in self.students:
            result += str(student) + '\n'
        return result


# Already created Student objects
s1 = Student(101, 'Gk', 23, 97)
s2 = Student(102, 'Saee', 24, 90)
s3 = Student(103, 'Rahul', 22, 85)

# Create College
c = College(5)

# Add already created students to College
c.AddStudent(s1)
c.AddStudent(s2)
c.AddStudent(s3)

# Operations
while True:
    print('\n1. Add Student')
    print('2. Search Student')
    print('3. Remove Student')
    print('4. Display Students')
    print('5. Exit')

    choice = int(input('Enter your choice: '))

    if choice == 1:
        sid = int(input('Enter Student ID: '))
        name = input('Enter Student Name: ')
        age = int(input('Enter Student Age: '))
        percentage = float(input('Enter Percentage: '))

        s = Student(sid, name, age, percentage)
        c.AddStudent(s)

    elif choice == 2:
        sid = int(input('Enter Student ID to Search: '))
        student = c.GetStudent(sid)
        if student:
            print('Student Found:', student)
        else:
            print('Student Not Found')

    elif choice == 3:
        sid = int(input('Enter Student ID to Remove: '))
        c.RemoveStudent(sid)

    elif choice == 4:
        print('\nStudents in College:')
        print(c)

    elif choice == 5:
        print('Thank you for visiting...!')
        break

    else:
        print('Invalid Choice')
