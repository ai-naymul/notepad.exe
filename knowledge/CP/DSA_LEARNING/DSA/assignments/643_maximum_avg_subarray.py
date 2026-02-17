from typing import List


## This is brute force solution this will take O(n^2) time complexity which will give TLE for large inputs.

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        return self.findmaxavgSlidingWindow(nums, k)
    
    # This is brute force solution this will take O(n^2) time complexity which will give TLE for large inputs.
    def findmaxavgBruteForce(self, nums: List[int], k: int) -> float:
        n = len(nums)
        max_sum = float("-inf")
        i = 0
        j = k - 1
        while j < n:
            curr_sum = 0
            for l in range(i, j + 1):
                curr_sum += nums[l]
            max_sum = max(max_sum, curr_sum)
            i += 1
            j += 1
        max_avg = max_sum / k
        return max_avg
    

    # this is sliding window solution this will take O(n) time complexity which is optimal solution.
    def findmaxavgSlidingWindow(self, nums: List[int], k: int) -> float:
        n = len(nums)
        max_sum = float("-inf")
        curr_sum = 0
        i = 0
        j = k - 1

        for l in range(i, j+1):
            curr_sum += nums[l]
        max_sum = curr_sum
        j += 1
        while j < n:
            curr_sum -= nums[i]
            i += 1
            curr_sum += nums[j]
            j += 1
            max_sum = max(max_sum, curr_sum)
        max_avg = max_sum / k
        return max_avg

        

sol =Solution()
print(sol.findMaxAverage([1, 12, -5, -6, 50, 3], 4))  # Output: 12.75
