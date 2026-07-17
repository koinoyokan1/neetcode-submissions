from functools import lru_cache

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @lru_cache(maxsize=None)
        def num(si=0, ti=0):
            if ti == len(t): return 1
            if si == len(s): return 0
            
            ans = 0
            if s[si] == t[ti]: ans += num(si+1, ti+1)
            ans += num(si+1, ti)
            
            return ans

        return num()