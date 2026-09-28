# 2. Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
# d. Constructor (Support both parameterized and parameterless)
# e. Destructor
# f. ShowBook 

class Product:
    def __init__(self, pid=0, pname='', price=0, quantity=0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def getID(self):
        return self.pid
    def setID(self, newID):
        self.pid = newID

    def getPName(self):
        return self.pname
    def setPName(self, newPN):
        self.pname = newPN

    def getPrice(self):
        return self.price
    def setPrice(self, newPr):
        self.price = newPr

    def getQuan(self):
        return self.quantity
    def setQuan(self, newQ):
        self.quantity = newQ

    def showProduct(self):
        return f'ID = {self.pid} | Name = {self.pname} | Price = {self.price} | Quantity = {self.quantity}'

    def __del__(self):
        print("Product object destroyed")

p = Product(102, 'Laptop' , 40000, 1)
print(p.showProduct())
