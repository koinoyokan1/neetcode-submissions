'''
n: num exist
len(nums)+1: invalid
p
'''
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > len(nums): nums[i] = len(nums) + 1

        print(nums)
        for n in nums:
            if abs(n) == len(nums) + 1: continue
            i = abs(n) - 1
            if nums[i] < 0: continue
            nums[i] = -nums[i]  

        for i in range(len(nums)):
            if nums[i] >= 0: return i+1  

        return len(nums) +1