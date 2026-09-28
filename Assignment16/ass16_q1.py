# 1. Create a class Book with members as bid,bname,price and author.Add following
# methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook
# d. Add static variable count and also maintain count of objects created.

class Book:
    count = 0             #static variable
    def __init__(self, bid=0, bname='', price=0, author=''):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author

        Book.count += 1

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


b1 = Book(1891,'The Buddha and his Dhamma' , 500, 'B R Ambedkar' )
b2 = Book(1212, 'Wings Of Fire', 400, 'APJ. Abdul Kalam')
print(b1.showBook())
print(b2.showBook())
print(f"Total Count of Book objects: {Book.count}")
