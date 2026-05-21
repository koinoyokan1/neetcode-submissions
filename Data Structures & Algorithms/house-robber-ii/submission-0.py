from functools import lru_cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        @lru_cache
        def _rob(i=0, startRobbed=False):
            if i >= len(nums): return 0
            if i == len(nums) - 1: 
                if startRobbed: return 0
                return nums[-1]
            
            return max(_rob(i+2, startRobbed) + nums[i], _rob(i+1, startRobbed))

        return max(_rob(2, True) + nums[0], _rob(1, False))
