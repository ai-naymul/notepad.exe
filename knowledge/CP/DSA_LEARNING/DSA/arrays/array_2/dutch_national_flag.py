#Approach one
nums = [0,1,0,1,2,0,2,0]
arr = []
def sort012(nums):
    c0 = 0
    c1 = 0
    c2 = 0
    for num in nums:
        if num == 0:
            c0 += 1
        elif num == 1:
            c1 += 1
        elif num == 2:
            c2 +=1
    index = 0
    for c in range(c0):
        nums[index] = 0
        index += 1

    for c in range(c1):
        nums[index] = 1
        index += 1

    for c in range(c2):
        nums[index] = 2
        index += 1
    return nums

array = sort012(nums=nums)
print(array)

# Appraoch 2 --> using the existing sort method
nums1 = [0,1,0,1,2,0,2,0]
def sortMethod(nums):
    nums.sort()
    return nums

array_sort = sortMethod(nums1)
print(array_sort)