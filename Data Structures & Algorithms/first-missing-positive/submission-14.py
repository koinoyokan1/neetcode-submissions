# 3, 18, -3, 2, 1 
# 3, 6, 6, 2, 1
# -3, -6, -6, 2, 1
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            n = nums[i]
            if n <= 0 or n > len(nums): nums[i] = len(nums)+1

        for i in range(len(nums)):
            n = abs(nums[i])
            if n == len(nums)+1: continue

            index = n - 1
            nums[index] = -abs(nums[index])

        print(nums)
        for i in range(len(nums)):
            if nums[i] > 0: return i+1
        
        return len(nums)+1
