from functools import lru_cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()

        @lru_cache(maxsize=None)
        def _hlp(i=0, amount=amount):
            if amount == 0: return 1
            if amount < 0: return 0

            ans = 0
            for j in range(i, len(coins)):
                if amount - coins[j] < 0: break
                ans += _hlp(j, amount - coins[j])

            return ans
        
        return _hlp()
