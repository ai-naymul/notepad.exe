from pickle import LIST
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    def twopointerapproach(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        while (i < j):
            if nums[i] + nums[j] == target:
                return [i, j]
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                j-=1
        return []

    def twosumpractice(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    def twopointerpractice(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(nums)
        i = 0
        j = len(num) - 1
        while (i < j):
            if nums[i] + nums[j] == target:
                return [i, j]
            elif nums[i] + nums[j] < target:
                i += 1
            elif nums[i] + nums[j] > target:
                j -= 1
        return []
        
if __name__ == "__main__":
    two_sum = Solution().twoSum(nums=[2, 7, 11, 15], target=9)
    print(two_sum)
