from functools import lru_cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()

        @lru_cache(maxsize=None)
        def _hlp(amount=amount):
            if amount == 0: return 0
            if amount < 0: return math.inf

            ans = math.inf
            for coin in coins:
                if amount - coin < 0: break
                ans = min(ans, _hlp(amount - coin) + 1)
            
            return ans
        
        ans = _hlp()
        if ans == math.inf: return -1
        return ans
