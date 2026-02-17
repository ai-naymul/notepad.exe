# in this one I didn't handled the duplicate case

nums = [-1,0,1,2,-1,-4]

def threeSum(self, nums):
        triplet = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        numbers = []
                        numbers.append(nums[i])
                        numbers.append(nums[j])
                        numbers.append(nums[k])
                        triplet.append(numbers)
        return triplet
values = threeSum(nums=nums)