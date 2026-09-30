# Create class television that has members to hold the model number ,screen size
# and price. Take a member function to take input from user, If more than 4 digits
# are entered for model number, if screen size is smaller than 12 inches or greater
# than 70 inches or if the price is negative or greater than 5000 Rs, then throw an
# exception.
# Write a main() that instantiates an object and allows the user to enter and display
# data. If exception is caught, replace all data member values with zero

class TelevisionException(Exception):
    pass

class Television:
    def __init__(self, modelno, size, price):
        self.modelno = modelno
        self.size = size
        self.price = price

    def validate(self):
        errors = []

        if len(str(self.modelno)) != 4:
            errors.append("Model number must be 4 digits")

        if self.size < 12 or self.size > 70:
            errors.append("Screen size must be between 12 and 70 inches")

        if self.price < 0 or self.price > 50000:
            errors.append("Price must be between 0 and 50000")

        if errors:
            raise TelevisionException("\n".join(errors))

def main():

    try:
        modelno = input("Enter model number: ")
        size = int(input("Enter screen size: "))
        price = float(input("Enter price: "))

        tv = Television(modelno, size, price)

        tv.validate()

        print("\nTelevision Details")
        print("Model Number:", tv.modelno)
        print("Screen Size:", tv.size)
        print("Price:", tv.price)

    except TelevisionException as e:

        print("\nExceptions:")
        print(e)

        modelno = 0
        size = 0
        price = 0

        print("\nValues after exception:")
        print("Model Number:", modelno)
        print("Screen Size:", size)
        print("Price:", price)

    except ValueError:
        print("Please enter valid numeric values.")

main()
