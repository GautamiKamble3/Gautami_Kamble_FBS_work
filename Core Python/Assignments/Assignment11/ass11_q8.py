# Print 1 to 100 in snakes and ladder pattern

num = 1
for row in range(1, 11):          # 10 rows
    if row % 2 != 0:              # odd row -> left to right
        for col in range(10):
            print(num, end='\t')
            num += 1
    else:                          # even row -> right to left
        # first collect the row's numbers
        row_nums = []
        for col in range(10):
            row_nums += [num]
            num += 1
        # then print them reversed
        for k in range(len(row_nums)-1, -1, -1):
            print(row_nums[k], end='\t')
    print()
