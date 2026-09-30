# 1. Create a class Emp (eid,ename,basic)
# 2. WAP a menu driven program to perform following operations using
# files :
# a. Add a record
# b. Search for a record using id
# c. Delete a record using id
# d. Edit a record using id.
# e. Display all records.

import pickle

class Emp:
    def __init__(self, eid, ename, basic):
        self.eid = eid
        self.ename = ename
        self.basic = basic

    def __str__(self):
        return f"ID: {self.eid} | Name: {self.ename} | Basic: {self.basic}"

def add_record():
    eid = int(input("Enter Employee ID: "))
    ename = input("Enter Employee Name: ")
    basic = float(input("Enter Basic Salary: "))

    e = Emp(eid, ename, basic)

    file = open("employees.dat", "ab")
    pickle.dump(e, file)
    file.close()

    print("Record added successfully.")

def display_records():
    try:
        file = open("employees.dat", "rb")

        while True:
            try:
                e = pickle.load(file)
                print(e)
            except EOFError:
                break

        file.close()

    except FileNotFoundError:
        print("No records found.")


def search_record():
    eid = int(input("Enter Employee ID to search: "))

    try:
        file = open("employees.dat", "rb")
        found = False

        while True:
            try:
                e = pickle.load(file)

                if e.eid == eid:
                    print("Record Found:")
                    print(e)
                    found = True
                    break

            except EOFError:
                break

        file.close()

        if not found:
            print("Record not found.")

    except FileNotFoundError:
        print("No records found.")


def delete_record():
    eid = int(input("Enter Employee ID to delete: "))

    try:
        file = open("employees.dat", "rb")
        records = []

        while True:
            try:
                e = pickle.load(file)

                if e.eid != eid:
                    records.append(e)

            except EOFError:
                break

        file.close()

        file = open("employees.dat", "wb")

        for e in records:
            pickle.dump(e, file)

        file.close()

        print("Record deleted successfully.")

    except FileNotFoundError:
        print("No records found.")


def edit_record():
    eid = int(input("Enter Employee ID to edit: "))

    try:
        file = open("employees.dat", "rb")

        records = []
        found = False

        while True:
            try:
                e = pickle.load(file)

                if e.eid == eid:
                    e.ename = input("Enter New Employee Name: ")
                    e.basic = float(input("Enter New Basic Salary: "))
                    found = True

                records.append(e)

            except EOFError:
                break

        file.close()

        file = open("employees.dat", "wb")

        for e in records:
            pickle.dump(e, file)

        file.close()

        if found:
            print("Record edited successfully.")
        else:
            print("Record not found.")

    except FileNotFoundError:
        print("No records found.")


def main():

    while True:

        print("\n----- Employee Menu -----")
        print("1. Add Record")
        print("2. Search Record")
        print("3. Delete Record")
        print("4. Edit Record")
        print("5. Display All Records")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_record()

        elif choice == 2:
            search_record()

        elif choice == 3:
            delete_record()

        elif choice == 4:
            edit_record()

        elif choice == 5:
            display_records()

        elif choice == 6:
            print("Program ended.")
            break

        else:
            print("Invalid choice.")


main()
