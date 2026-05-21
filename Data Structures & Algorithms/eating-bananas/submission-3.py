class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        ans = 1000000001

        while left <= right:
            k = math.ceil((left + right)/2)
            hrsNeeded = 0
            for pile in piles:
                hrsNeeded += math.ceil(pile/k)
            if hrsNeeded > h:
                left = k + 1
            else:
                ans = min(ans, k)
                right = k - 1
        
        return ans