from functools import lru_cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(maxsize=None)
        def _hlp(i=0, target=target):
            if i == len(nums):
                if target == 0: return 1
                return 0
            

            ans = _hlp(i+1, target+nums[i])
            return ans + _hlp(i+1, target-nums[i])
        return _hlp()