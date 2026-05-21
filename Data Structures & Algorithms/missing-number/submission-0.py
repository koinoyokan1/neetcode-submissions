# 1,2,3
# a = 6
# e = 6
# 0
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        actualAddn = sum(nums)
        expectedAddn = (len(nums) * (len(nums) + 1))//2

        return expectedAddn - actualAddn