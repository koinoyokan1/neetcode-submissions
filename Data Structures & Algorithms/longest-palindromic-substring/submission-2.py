from functools import lru_cache
class Solution:
    def longestPalindrome(self, s: str) -> str:
        @lru_cache(maxsize=None)
        def _hlp(i=0,j=0):
            if i == j: return True

            if s[i] != s[j]: return False
            if j == i+1 and s[i] == s[j]: return True
            return _hlp(i+1,j-1)
        
        mxStr = (0,0)

        for i in range(len(s)):
            for j in range(len(s)-1, i-1, -1):
                if _hlp(i,j):
                    if j - i + 1 > mxStr[1] - mxStr[0] + 1: mxStr = (i,j)
                    break
        return s[mxStr[0]:mxStr[1]+1]
        

