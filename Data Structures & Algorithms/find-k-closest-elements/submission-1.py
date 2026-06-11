# 2 3 4
# k=3, x = 1
# 
import bisect

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - 1

        ans = []

        ri = bisect.bisect_left(arr, x)
        li = ri - 1
        dist = 0

        for i in range(k):
            if ri < len(arr) and abs(x-arr[li]) > abs(x-arr[ri]):
                ans.append(arr[ri])
                ri += 1
            else:
                ans.append(arr[li])
                li -= 1

        return sorted(ans)