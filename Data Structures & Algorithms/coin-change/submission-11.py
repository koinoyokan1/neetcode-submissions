from functools import lru_cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()

        @lru_cache(maxsize=None)
        def _cg(amt=amount):
            if amt == 0: return 0
            if amt < 0: return math.inf

            ans = math.inf
            for coin in coins:
                if amt - coin < 0: break
                ans = min(ans, _cg(amt-coin) + 1)
            
            return ans

        ans = _cg()
        if ans == math.inf: return -1
        return ans