from functools import lru_cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache
        def _hlp(i=0, j=0):
            if i == len(text1) or j == len(text2): return 0

            if text1[i] == text2[j]: return 1 + _hlp(i+1, j+1)
            return max(_hlp(i+1, j), _hlp(i, j+1))
        
        return _hlp()