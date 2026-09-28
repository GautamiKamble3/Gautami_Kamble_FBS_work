# 2. Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
# e. Constructor (Support both parameterized and parameterless)
# f. Destructor
# g. ShowBook
# h. Add static member discount.
# i. Provide methods for applying discount on price of product.

class Product:

    # static variable
    discount = 10

    # Constructor - parameterized and parameterless
    def __init__(self, pid=0, pname='', price=0, quantity=0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    # Getter and Setter methods
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

    # Apply discount
    def applyDiscount(self):
        self.price = self.price - (self.price * Product.discount / 100)

    # Display Product
    def ShowProduct(self):
        print(f'ID = {self.pid} | Name = {self.pname} | '
              f'Price = {self.price} | Quantity = {self.quantity}')

    # Destructor
    def __del__(self):
        print("Product object destroyed")

p = Product(102, 'Laptop', 40000, 1)

p.ShowProduct()

p.applyDiscount()

print("After Discount on Price:")
p.ShowProduct()
