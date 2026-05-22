class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cnReach = 0

        for i in range(len(nums)):
            if i > cnReach: return False
            num = nums[i]
            cnReach = max(cnReach, i + num)
            if cnReach >= len(nums) - 1: return True
        
        return False
