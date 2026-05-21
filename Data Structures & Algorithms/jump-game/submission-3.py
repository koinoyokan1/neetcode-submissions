class Solution:
    def canJump(self, nums: List[int]) -> bool:
        canReach = 0

        for i in range(len(nums)):
            if i > canReach: return False
            canReach = max(canReach, i + nums[i])
            print(canReach)

        if canReach >= len(nums) - 1: return True
        return False
