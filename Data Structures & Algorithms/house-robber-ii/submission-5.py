from functools import lru_cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache()
        def _r(i=0, start=False):
            if i >= len(nums): return 0
            if i == len(nums) - 1: 
                if start: return 0
                return nums[i]
            
            return max(_r(i+1, start), _r(i+2, start) + nums[i])
        
        return max(_r(2, True) + nums[0], _r(1, False))