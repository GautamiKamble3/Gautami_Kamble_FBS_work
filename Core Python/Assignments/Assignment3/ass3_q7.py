# Write a program to check if user has entered correct userid and password.

userid = input("Enter User ID: ")
password = input("Enter Password: ")

if userid == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid User ID or Password")
