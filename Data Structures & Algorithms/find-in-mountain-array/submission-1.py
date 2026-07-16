# 1 2 3 4 3 1
# 
class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        ln = mountainArr.length()
        def findHighestInRotated():
            left, right = 0, ln-1

            while left <= right:
                mid = (left+right)//2
                if mid > 0 and mid < ln-1 and mountainArr.get(mid-1) < mountainArr.get(mid) > mountainArr.get(mid+1):
                    return mid
                if mid > 0 and mountainArr.get(mid-1) < mountainArr.get(mid):
                    left = mid + 1
                else:
                    right = mid - 1

            return -1

        hindex = findHighestInRotated()

        def bsearch(left, right, inc=True):
            while left <= right:
                mid = (left+right)//2
                if mountainArr.get(mid) == target:
                    return mid 
                if (inc and mountainArr.get(mid) < target) or (not inc and mountainArr.get(mid) > target):
                    left = mid + 1
                else:
                    right = mid - 1

            return -1

        ans = bsearch(0, hindex)
        if ans != -1: return ans
        return bsearch(hindex+1, ln-1, False)