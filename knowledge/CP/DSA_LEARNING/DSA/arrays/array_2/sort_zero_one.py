# approach two

nums = [0, 1, 0, 1, 1, 0, 1, 0, 0, 1]
zeroCount = []
oneCount = []
for i in range(len(nums)):
    if nums[i] == 0:
        zeroCount.append(0)
    else:
        oneCount.append(1)
result = zeroCount + oneCount
print(result)