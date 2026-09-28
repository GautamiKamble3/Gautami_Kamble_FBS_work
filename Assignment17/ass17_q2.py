# 2. Create a derived class from Student as EnggStudent with :
# a. Data members as :
# i. Branch
# ii. InternalMarks

# b. Add the following methods :
# i. Parameterized constructor
# ii. Display
# iii. Accept
# iv. override Method CalculateRank
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


# Student class ends here...............


class EnggStudent(Student):

    def __init__(self, sid, sname, sage, sper, branch, inMarks):
        super().__init__(sid, sname, sage, sper)
        self.branch = branch
        self.inMarks = inMarks

    def getBranch(self):
        return self.branch

    def setBranch(self, newB):
        self.branch = newB

    def getMarks(self):
        return self.inMarks

    def setMarks(self, newM):
        self.inMarks = newM

    def display(self):
        print(self)

    def accept(self):
        super().accept()
        self.branch = input('Enter Branch: ')
        self.inMarks = float(input('Enter Internal Marks: '))

    def calculateRank(self):
        total = self.sper + self.inMarks

        if total >= 175:
            return 'First'
        elif total >= 150:
            return 'Second'
        elif total >= 125:
            return 'Third'
        elif total >= 100:
            return 'Pass'
        else:
            return 'Fail'

    def __str__(self):
        return super().__str__() + f' | Branch Name = {self.branch} | Internal Marks = {self.inMarks}'


e1 = EnggStudent(101, 'Saee Chavan', 23, 97, 'Computer Science', 18)
e1.display()
print('Rank:', e1.calculateRank())

e2 = EnggStudent(0, '', 0, 0, '', 0)
e2.accept()
e2.display()
print('Rank:', e2.calculateRank())
