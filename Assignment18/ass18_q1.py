# Python Assignment – (Operator Overloading)
# 1. Create a class Complex Number with data members as real and imag and add
# following methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator

class ComplexNumber:
    def __init__(self, realN, imgN):
        self.realN = realN
        self.imgN = imgN

    def getRN(self):
        return self.realN
    def setRN(self, newRN):
        self.realN = newRN

    def getIN(self):
        return self.imgN
    def setIN(self, newIN):
        self.imgN = newIN

    def __del__(self):
        print('Object of Complex number is Destroyed...')

    def __add__(self, other):
        real = self.realN + other.realN
        image = self.imgN + other.imgN
        return ComplexNumber(real, image)

    def __sub__(self, other):
        real = self.realN - other.realN
        image = self.imgN - other.imgN
        return ComplexNumber(real, image)

    def __str__(self):
        return f'{self.realN} + {self.imgN}i'

c1 = ComplexNumber(10,20) 
c2 = ComplexNumber(5,10)

c3 = c1+c2
print('Addition: ', c3)

c4 = c1 - c2
print('Subtraction: ',c4)
