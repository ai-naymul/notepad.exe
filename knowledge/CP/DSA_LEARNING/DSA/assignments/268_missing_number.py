# from typing import List
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         sorted_nums = sorted(nums)
#         for i in range(len(sorted_nums)):
#             if sorted_nums[i] != i:
#                 return i
        


from typing import List
# class Solution:
#     def missingNumbeSortingMethod(self, nums: List[int]) -> int:
#         sorted_nums = sorted(nums)
#         for i in range(len(sorted_nums)+1):
#             print(i)
#             if i not in sorted_nums:
#                 return i

# missing_number = Solution()
# print(missing_number.missingNumbeSortingMethod([0, 1]))  # Output: 2

class Solution:
    def missingNumberXORMethod(self, nums: list[int]) -> int:
        n = len(nums)
        xor_all = 0
        xor_nums = 0

        for i in range(n + 1):
            xor_all ^= i
            print(f"xor_all: {xor_all} after {i}")
        
        for num in nums:
            xor_nums ^= num
            print(f"xor_nums: {xor_nums} after {num}")
        
        return xor_all ^ xor_nums

missing_number = Solution()
print(missing_number.missingNumberXORMethod([0, 1]))  # Output: 2