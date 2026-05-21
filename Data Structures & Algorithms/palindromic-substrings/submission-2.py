from functools import lru_cache
class Solution:
    def countSubstrings(self, s: str) -> int:
        @lru_cache(maxsize=None)
        def _hlp(i=0,j=0):
            if i == j: return True

            if s[i] != s[j]: return False
            if j == i+1 and s[i] == s[j]: return True
            return _hlp(i+1,j-1)
        
        ans = 0
        for i in range(len(s)):
            for j in range(len(s)-1, i-1, -1):
                if _hlp(i,j): ans += 1
        return ans   