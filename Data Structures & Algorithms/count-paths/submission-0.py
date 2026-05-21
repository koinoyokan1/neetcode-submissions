from functools import lru_cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @lru_cache(maxsize=None)
        def _hlp(i=0, j=0):
            if i == m-1 and j == n-1: return 1
            if i == m or j == n: return 0

            a = _hlp(i+1, j)
            b = _hlp(i, j+1)
            return a + b
        
        return _hlp()
