from functools import lru_cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @lru_cache(maxsize=None)
        def _hlp(i=0,j=0,k=0):
            if i == len(s1) and j == len(s2) and k == len(s3): return True
            if k == len(s3): return False

            ans = False
            if i < len(s1) and s1[i] == s3[k]:
                ans = _hlp(i+1, j, k+1)
            if j < len(s2) and s2[j] == s3[k]:
                ans = ans or _hlp(i, j+1, k+1)
            return ans

        return _hlp()
