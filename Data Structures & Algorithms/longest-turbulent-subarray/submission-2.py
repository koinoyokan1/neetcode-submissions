from functools import lru_cache
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) <= 1: return len(arr)

        @lru_cache
        def mx(i):
            if i == len(arr)-1:
                return 1, 0

            if arr[i] == arr[i+1]:
                return 1, 0

            inc = 1 if arr[i] < arr[i+1] else -1

            cnt, nextInc = mx(i+1)

            if inc == nextInc: return 2, inc
            else: return cnt + 1, inc
            
        mxLen = 0
        for i in range(len(arr)):
            ans, _ = mx(i)
            mxLen = max(mxLen, ans) 

        return mxLen
            