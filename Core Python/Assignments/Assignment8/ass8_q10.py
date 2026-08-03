# Write a program to check if entered year is a leap year or not.

def leap_year(y):
    
    if(y % 400 == 0):
        print('Leap Year')
    elif(y % 4 == 0 and y % 100 != 0):
        print('Leap Year')
    else:
        print('Not Leap Year')

y = int(input('Enter year: '))
leap_year(y)
