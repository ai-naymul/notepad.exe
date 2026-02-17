from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums eeeeeeee(nums)
        for i in range(len(nums)):
            if i == nums[i]:
                continue
            else:
                return i

        return len(nums)





if __name__ == "__main__":
    nums = [3,0,1]
    sol = Solution().missingNumber(nums)
    print(sol)
