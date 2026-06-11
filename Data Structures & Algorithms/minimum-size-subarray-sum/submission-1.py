# 2 1 5 1 5 3

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0

        mn = len(nums) + 1
        curr = 0

        for r in range(len(nums)):
            curr += nums[r]
            while curr >= target:
                mn = min(mn, r - l + 1)
                curr -= nums[l]
                l += 1
        if mn == len(nums) + 1: return 0
        return mn
