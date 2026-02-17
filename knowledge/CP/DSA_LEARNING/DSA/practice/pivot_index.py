from typing import List


class Solution:
    def prefixpivotIndex(self, nums: List[int]) -> int:
        lsum = []
        rsum = []
        for i in range(len(nums)):
            lsum = sum(nums[:i])
            rsum = sum(nums[i+1:])
            if lsum == rsum:
                return i




    def pivotindex(self, nums: List[int]) -> int:
        lsum = [0] * len(nums)
        rsum = [0] * len(nums)
        for i in range(1, len(nums)):
            lsum[i] = lsum[i-1] + nums[i-1]
        for i in range(len(nums) - 2, -1, -1):
            rsum[i] = rsum[i+1] + nums[i+1]
        for i in range(len(nums)):
            if lsum[i] == rsum[i]:
                return i
        return -1



if __name__ == "__main__":
    nums = [1,7,3,6,5,6]
    sol = Solution().pivotindex(nums)
    print(sol)
