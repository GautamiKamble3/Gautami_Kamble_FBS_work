# Python Program to Merge Two Lists and Sort it

def mergeList(li1,li2):
    li3 = li1 + li2
    print(f'Merge list1 and list2 = list3 {li3}')
    li3.sort()
    print(f'Sort list3 : {li3}')

li1 = [7,14,21,28,30]
li2 = [5,10,15,20,25]

print(f'list 1 : {li1}')
print(f'list 2 : {li2}')

li3=[]
result = mergeList(li1,li2)
