from functools import lru_cache
import math
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @lru_cache(maxsize=None)
        def _lengthOfLIS(i=0, mx=-math.inf):
            if i == len(nums): return 0
            
            ans = 0
            if nums[i] > mx:
                ans = _lengthOfLIS(i+1, nums[i])+1
            return max(_lengthOfLIS(i+1, mx), ans)
        return _lengthOfLIS()
        