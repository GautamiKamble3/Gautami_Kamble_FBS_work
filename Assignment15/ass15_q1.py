# 1. Create a class Book with members as bid,bname,price and author.Add following
# methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook 

class Book:
    def __init__(self, bid=0, bname='', price=0, author=''):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author

    def getId(self):
        return self.bid
    def setId(self,new_id):
        self.bid = new_id

    def getName(self):
        return self.bname
    def setName(self, newN):
        self.bname = newN

    def getPrice(self):
        return self.price
    def setPrice(self, newP):
        self.price = newP

    def getAu(self):
        return self.author
    def setAu(self, newA):
        self.author = newA

    def showBook(self):
        return f'Book id = {self.bid} | Book Name = {self.bname} | Book price = {self.price} | Book Author = {self.author}'

    def __del__(self):
        print("Book object destroyed")

b = Book(1891,'The Buddha and his Dhamma' , 500, 'B R Ambedkar' )
print(b.showBook())
