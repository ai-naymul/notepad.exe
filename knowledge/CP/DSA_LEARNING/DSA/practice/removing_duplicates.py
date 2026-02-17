from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        j = 0
        while i < len(nums):
            if nums[i] == nums[j]:
                i += 1
            else:
                j += 1
                nums[j] = nums[i]
                i += 1
        return j+1

if __name__ =="__main__":
    nums = [1,1,2]
    sol = Solution().removeDuplicates(nums)
    print(sol)