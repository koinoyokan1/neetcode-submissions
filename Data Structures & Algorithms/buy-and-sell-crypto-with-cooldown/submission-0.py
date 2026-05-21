from functools import lru_cache
class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        
        @lru_cache()
        def _hlp(i=0, bought=False):
            if i >= len(prices): return 0

            ans = math.inf

            if bought: 
                ans = _hlp(i+2, False) + prices[i]
            else: 
                ans = _hlp(i+1, True) - prices[i]

            return max(ans, _hlp(i+1, bought))
        
        return _hlp()
