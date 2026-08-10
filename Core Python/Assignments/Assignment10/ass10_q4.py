# 4. Write a program to reverse the list.

li = [10, 20, 30, 40, 50, 60, 70]

start = 0
end = len(li) - 1

while (start < end):
    temp = li[start]
    li[start] = li[end]
    li[end] = temp

    start += 1
    end -= 1

print(f'Reverse of the list is : {li}')
