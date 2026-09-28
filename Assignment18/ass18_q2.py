# 2. Create a class Distance with data members as km,m and cm and add following
# methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator

class Distance:
    def __init__(self, km, m ,cm):
        self.km = km
        self.m = m
        self.cm = cm

    def getKm(self):
        return self.km
    def setKm(self, newKm):
        self.km = newKm

    def getM(self):
        return self.m
    def setM(self, new_m):
        self.m = new_m

    def getCm(self):
        return self.cm
    def setCm(self, newCm):
        self.cm = newCm

    def __del__(self):
        print('Object of Distance is Destroyed...')

    def __add__(self, other):
        km = self.km + other.km
        m = self.m + other.m
        cm = self.cm + other.cm

        if cm >= 100:
            m = m + cm // 100
            cm = cm % 100

        if m >= 1000:
            km = km + m // 1000
            m = m % 1000

        return Distance(km, m, cm)

    def __sub__(self, other):
        km = self.km - other.km
        m = self.m - other.m
        cm = self.cm - other.cm

        if cm < 0:
            m = m - 1
            cm = cm + 100

        if m < 0:
            km = km - 1
            m = m + 1000

        return Distance(km, m, cm)

    def __str__(self):
        return f'{self.km}  km | {self.m} m | {self.cm} cm'

d1 = Distance(5, 500, 80)
d2 = Distance(2, 700, 50)

d3 = d1 + d2
print('Addition: ', d3)

d4 = d1 - d2
print('Subtraction: ',d4)

