from functools import lru_cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        mxVal = math.ceil(sum(nums)/2)

        @lru_cache(maxsize=None)
        def _hlp(i=0, diff=0):
            if i == len(nums): return diff == 0

            ans = False
            if diff +nums[i] <= mxVal:
                ans = _hlp(i+1, diff+nums[i])
            if diff - nums[i] >= -mxVal:
                ans |= _hlp(i+1, diff-nums[i])
            
            return ans

        return _hlp()
