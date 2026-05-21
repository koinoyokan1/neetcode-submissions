from functools import lru_cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @lru_cache(maxsize=None)
        def _change(i=0, amount=amount):
            if amount < 0: return 0 
            if amount == 0: return 1

            ans = 0
            for j in range(i, len(coins)):
                ans += _change(j, amount-coins[j])
            
            return ans

        return _change()