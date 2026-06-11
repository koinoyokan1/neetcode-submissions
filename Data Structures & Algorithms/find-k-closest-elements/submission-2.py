# 2 3 4
# k=3, x = 1
# 
import bisect

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - 1

        ri = bisect.bisect_left(arr, x)
        li = ri-1

        while ri - li - 1 < k:
            if ri >= len(arr):
                li -= 1
            elif li < 0:
                ri += 1
            elif abs(x - arr[ri]) >= abs(x - arr[li]):
                li -= 1
            else:
                ri += 1

        return arr[li+1:ri]
