# 3. Create a class MedicalStudent inherited from Student with following:
# i. Data members :Specialization
# ii. MarksOfInternship

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

# Student class ends here................

class MedicalStudent(Student):

    def __init__(self, sid, sname, sage, sper, special, intern):
        super().__init__(sid, sname, sage, sper)
        self.special = special
        self.intern = intern

    def getSpecial(self):
        return self.special

    def setSpecial(self, newSp):
        self.special = newSp

    def getIntern(self):
        return self.intern

    def setIntern(self, newIn):
        self.intern = newIn

    def display(self):
        print(self)

    def accept(self):
        super().accept()
        self.special = input('Enter Specialization: ')
        self.intern = float(input('Enter Marks of Internship: '))

    def calculateRank(self):
        total = self.sper + self.intern

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
        return super().__str__() + f' | Specialization = {self.special} | Marks of Internship = {self.intern}'


# Object

m1 = MedicalStudent(102, 'Gk', 24, 90, 'Cardiology', 18)
m1.display()
print('Rank:', m1.calculateRank())

m2 = MedicalStudent(0, '', 0, 0, '', 0)
m2.accept()
m2.display()
print('Rank:', m2.calculateRank())
