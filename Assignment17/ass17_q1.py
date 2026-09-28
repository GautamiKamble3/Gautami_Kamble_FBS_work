# Python Inheritance Assignment

# 1. Create a class Student with following
# a. data members :
# i. StudentId
# ii. Name
# iii. Age
# iv. Percentage

# b. Add the following methods :
# i. Parameterized constructor
# ii. Display
# iii. Accept
# iv. Method CalculateRank
# v. Override __str__ Method

class Student:
    def __init__(self, sid, sname, sage, sper):
        self.sid = sid
        self.sname = sname
        self.sage = sage
        self.sper = sper

    def getSid(self):
        return self.sid
    def setSid(self, newId):
        self.sid = newId

    def getSName(self):
        return self.sname
    def setSName(self, newN):
        self.sname = newN

    def getSage(self):
        return self.sage
    def setSage(self, newAge):
        self.sage = newAge

    def getSper(self):
        return self.sper
    def setSper(self, newP):
        self.sper = newP

    def display(self):
        print(self)

    def accept(self):
        self.sid = int(input('Enter Student ID: '))
        self.sname = input('Enter Student Name: ')
        self.sage = int(input('Enter Student Age: '))
        self.sper = float(input('Enter Student Percentage: '))

    def calculateRank(self):
        if self.sper >= 75:
            return 'First'
        elif self.sper >= 60:
            return 'Second'
        elif self.sper >= 50:
            return 'Third'
        elif self.sper >= 35:
            return 'Pass'
        else:
            return 'Fail'

    def __str__(self):
        return f'ID = {self.sid} | Name = {self.sname} | Age = {self.sage} | Percentage = {self.sper}'
    

s1 = Student(101, 'Gk', 23, 97)
s1.display()
print('Rank: ', s1.calculateRank())

