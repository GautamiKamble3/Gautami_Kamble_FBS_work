# Write a program to accept an integer amount from user and tell minimum
# number of notes needed for representing that amount. 

a=int(input('Enter amount:'))

notes=[2000,500,200,100,50,20,10]

n2000=a//2000
amount=a%2000

n500=amount//500
amount=amount%500

n200=amount//200
amount=amount%200

n100=amount//100
amount=amount%100

n50=amount//50
amount=amount%50

n20=amount//20
amount=amount%20

n10=amount//10
amount=amount%10

total_notes=n2000+n500+n200+n100+n50+n20+n10

print(f'2000:{n2000}')
print(f'500:{n500}')
print(f'200:{n200}')
print(f'100:{n100}')
print(f'50:{n50}')
print(f'20:{n20}')
print(f'10:{n10}')
print(f'total notes is:{total_notes}')
