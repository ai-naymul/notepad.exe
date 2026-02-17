nums = [10, 20,30,40]
combination = 0
for i in nums:
    for j in nums:
        for k in nums:
            print(i,j,k)
            combination += 1
print(combination)