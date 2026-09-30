from SY.symarks import SYMARKS
from TY.tymarks import TYMarks

class Student: 
    def __init__(self, rollno, name, SYMarks, TYMarks):
        self.rollno = rollno
        self.name = name
        self.SYMarks = SYMarks
        self.TYMarks = TYMarks

    def calculate_grade(self):

        total = self.SYMarks.computer + self.TYMarks.theory + self.TYMarks.practical
        percentage = (total/300)*100

        if percentage >= 70:
            grade = "A"
        elif(percentage >= 60):
            grade = "B"
        elif(percentage >= 50):
            grade = "C"
        elif(percentage >= 40):
            grade = "Pass"
        else:
            grade = "Fail"

        return grade

    def __str__(self):
        return f"Roll No: {self.rollno}\nName: {self.name}\n" \
               f"SY Computer: {self.SYMarks.computer}\n" \
               f"TY Theory: {self.TYMarks.theory}\n" \
               f"TY Practical: {self.TYMarks.practical}\n" \
               f"Grade: {self.calculate_grade()}"

sy = SYMARKS(78, 84, 90)
ty = TYMarks(85, 76)

s = Student(7, "Gautami", sy, ty)

print(s)
