nums = [2, 7, 11, 6, 15, 3]
target = 9
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        print((i,j))