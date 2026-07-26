# Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate. 


attempt = 1
while(attempt <= 3):

    user_id = input('Enter your username: ')
    password = int(input('Enter your password: '))

    if user_id == 'gautami7' and password == 1515 :
        print('User Login Successfull!!')
        break
    else:
        print(f'Attempts done:  {attempt}')
        attempt += 1

if attempt > 3:
    print('Attemps finished ')
