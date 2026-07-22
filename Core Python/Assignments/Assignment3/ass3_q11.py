# Accept age of five people and also per person ticket amount and then calculate total
# amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.


# First person
age1=int(input('Enter age person1:'))
tkprice1=float(input('Enter ticket price:'))
totalprice=0

if(age1<=12):
    totalprice=totalprice+(tkprice1*0.30)
elif(age1>59):
    totalprice=totalprice+(tkprice1*0.50)
else:
    totalprice=totalprice+tkprice1


# Second person
age2=int(input('Enter age person2:'))
tkprice2=float(input('Enter ticket price:'))
totalprice=0

if(age1<=12):
    totalprice=totalprice+(tkprice2*0.30)
elif(age1>59):
    totalprice=totalprice+(tkprice2*0.50)
else:
    totalprice=totalprice+tkprice2



# third person
age3=int(input('Enter age person3:'))
tkprice3=float(input('Enter ticket price:'))
totalprice=0

if(age3<=12):
    totalprice=totalprice+(tkprice3*0.30)
elif(age3>59):
    totalprice=totalprice+(tkprice3*0.50)
else:
    totalprice=totalprice+tkprice3


# fourth person
age4=int(input('Enter age person4:'))
tkprice4=float(input('Enter ticket price:'))
totalprice=0

if(age4<=12):
    totalprice=totalprice+(tkprice4*0.30)
elif(age1>59):
    totalprice=totalprice+(tkprice4*0.50)
else:
    totalprice=totalprice+tkprice4



# fifth person
age5=int(input('Enter age person5:'))
tkprice5=float(input('Enter ticket price:'))
totalprice=0

if(age5<=12):
    totalprice=totalprice+(tkprice5*0.30)
elif(age5>59):
    totalprice=totalprice+(tkprice5*0.50)
else:
    totalprice=totalprice+tkprice5

print(f'Total ticket price of 5 persons is ={totalprice}')
