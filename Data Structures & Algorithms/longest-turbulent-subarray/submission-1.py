from functools import lru_cache
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) <= 1: return len(arr)

        @lru_cache(None)
        def mx(i):
            if i == len(arr)-1:
                return 1, 0

            if arr[i] == arr[i+1]:
                return 1, 0

            sign = 1 if arr[i] < arr[i+1] else -1

            cnt, inc = mx(i+1)

            if sign * inc == -1:
                return cnt + 1, sign
            else:
                return 2, sign
            
        mxLen = 0
        for i in range(len(arr)):
            ans, _ = mx(i)
            mxLen = max(mxLen, ans) 

        return mxLen
            