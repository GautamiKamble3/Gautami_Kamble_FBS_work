# Write a program to check if person is eligible to marry or not (male age >=21 and
# female age>=18)

gender = input('Enter your gender(m/f): ')
age = int(input('Enter your age: '))

if(gender == 'f'):
    if(age >= 18):
        print(f'Girl is Eligible for Marriage')
    else: 
        print(f'Girl is Not Eligible for Marriage')
else:
    if(age >= 21):
        print(f'Boy is Eligible for Marriage')
    else:
        print(f'Boy is Not Eligible for Marriage')
