# Accept no. of passengers from user and per ticket cost. Then accept age of each passenger and
# then calculate total amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

num=int(input('Enter number of passengers:'))

total=0

for i in range(1,num+1):
    age=int(input('Enter age of person:'))
    tkcost=float(input('Enter ticket cost:'))

    if(age<=12):
        total=total+(tkcost*0.30)
    elif(age>=59):
        total=total+(tkcost*0.50)
    else:
        total=total+tkcost

print(f'total amount to ticket to travel={total}')
