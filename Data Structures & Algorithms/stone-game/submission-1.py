from functools import lru_cache

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @lru_cache(maxsize=None)
        def sg(l=0, r=len(piles)-1, aliceTurn=True):
            if l >= r: return 0

            mx = 0
            if aliceTurn:
                mx = max(mx, sg(l+1, r, False) + piles[l])
                mx = max(mx, sg(l, r-1, False) + piles[r])
                return mx
            
            mn = math.inf
            mn = min(mn, sg(l+1, r, True))
            min(mn, sg(l, r-1, True))

            return mn
        
        return sg() > 0


