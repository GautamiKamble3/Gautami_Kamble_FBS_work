# 3. Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# j. Constructor (Support both parameterized and parameterless)
# k. Destructor
# l. ShowBook
# m. For each size of shirt price should change by 10%.
# (eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and
# xlarge=1300) Use static concept.

class Shirt:

    sizeIncrease = 10

    def __init__(self, sid=0, sname='', stype='', price=0, size=''):
        self.sid = sid
        self.sname = sname
        self.stype = stype
        self.price = price
        self.size = size

    def getID(self):
        return self.sid

    def setID(self, newId):
        self.sid = newId

    def getName(self):
        return self.sname

    def setName(self, newN):
        self.sname = newN

    def getType(self):
        return self.stype

    def setType(self, newT):
        self.stype = newT

    def getPrice(self):
        return self.price

    def setPrice(self, newPr):
        self.price = newPr

    def getSize(self):
        return self.size

    def setSize(self, newS):
        self.size = newS

    def applySizePrice(self):
        if self.size.lower() == 'small':
            self.price = self.price

        elif self.size.lower() == 'medium':
            self.price = self.price + (self.price * Shirt.sizeIncrease / 100)

        elif self.size.lower() == 'large':
            self.price = self.price + (self.price * Shirt.sizeIncrease * 2 / 100)

        elif self.size.lower() == 'xlarge':
            self.price = self.price + (self.price * Shirt.sizeIncrease * 3 / 100)

    def showShirt(self):
        return f'ID = {self.sid} | Name = {self.sname} | Type = {self.stype} | Price = {self.price} | Size = {self.size}'

    def __del__(self):
        print('Shirt Object Destroyed.')


s = Shirt(111, 'Zudio', 'Formal', 3000, 'large')

s.applySizePrice()

print(s.showShirt())
