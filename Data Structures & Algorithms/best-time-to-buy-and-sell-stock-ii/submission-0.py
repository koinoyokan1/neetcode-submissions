'''
1 4 5

'''
from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @lru_cache(maxsize=None)
        def mp(i=0, buy=True):
            if i == len(prices): return 0

            ans = mp(i+1, buy)
            if buy:
                ans = max(ans, mp(i+1, False) - prices[i])
            else:
                ans = max(ans, mp(i+1, True) + prices[i])
            
            return ans
        
        return mp()