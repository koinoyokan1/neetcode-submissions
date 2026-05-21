from functools import lru_cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache()
        def _rob(i):
            if i >= len(nums): return 0
            
            ans = 0
            ans = _rob(i+2) + nums[i]
            ans = max(ans, _rob(i+1))
            return ans

        return max(_rob(0), _rob(1))
