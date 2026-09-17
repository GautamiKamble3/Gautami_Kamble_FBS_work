
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def cal_toll(self, persons):
        pass

class TwoWheeler(Vehicle):
    def cal_toll(self, persons):
        toll = 20
        if persons > 2:
            extra_per = persons - 2
            toll = toll + (extra_per * 10)
        return toll

class ThreeWheeler(Vehicle):
    def cal_toll(self, persons):
        toll = 30
        if persons > 3:
            extra_per = persons - 3
            toll = toll + (extra_per * 20)

        return toll


class FourWheeler(Vehicle):
    def cal_toll(self, persons):
        toll = 40
        if persons > 4:
            extra_pers = persons - 4
            toll = toll + (extra_pers * 40)
        return toll

class HeavyVehicle(Vehicle):
    def cal_toll(self, persons):
        toll = 60
        if persons > 6:
            extra_pers = persons - 6
            toll = toll + (extra_pers * 100)
        return toll

while (True):
    print("******** TOLL PLAZA **********")
    print("1. Two Wheeler")
    print("2. Three Wheeler")
    print("3. Four Wheeler")
    print("4. Heavy Vehicle")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Thank you for visiting us!")
        break

    persons = int(input("Enter number of persons: "))

    if choice == 1:
        vehicle = TwoWheeler()

    elif choice == 2:
        vehicle = ThreeWheeler()

    elif choice == 3:
        vehicle = FourWheeler()

    elif choice == 4:
        vehicle = HeavyVehicle()

    else:
        print("Invalid choice......")
        continue

    print("Total Toll = Rs.", vehicle.cal_toll(persons))
