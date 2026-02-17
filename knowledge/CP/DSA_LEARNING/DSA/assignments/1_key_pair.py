# this problem is known as two sum problem
# tried two pointer apporach sometime it fails due to sorting and other issues.
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        low = 0
        high = len(nums) - 1
        while low < high:
            current_sum = nums[low] + nums[high]
            if current_sum == target:
                return [low, high]
            elif current_sum > target:
                high -= 1
            else:
                low += 1

sol = Solution()
print(sol.twoSum([3,2,4], 6))  # Output: [2, 7]


# there is another solution using hashmap
class SolutionHashMap:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i

sol_hash_map = SolutionHashMap()
print(sol_hash_map.twoSum([3,2,4], 6))  # Output: [1, 2]
# this is the best solution with O(n) time complexity