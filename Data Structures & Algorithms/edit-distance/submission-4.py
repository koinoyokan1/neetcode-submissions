from functools import lru_cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(maxsize=None)
        def _hlp(i1=0, i2=0):
            if i1 == len(word1) and i2 == len(word2): return 0
            if i2 == len(word2): return len(word1) - i1
            if i1 == len(word1): return len(word2) - i2

            ans = math.inf
            if word1[i1] == word2[i2]:
                ans = _hlp(i1+1, i2+1)

            ans = min(ans, _hlp(i1+1, i2+1) + 1)

            ans = min(ans, _hlp(i1+1, i2) + 1)
            return min(ans, _hlp(i1, i2+1) + 1)

        return _hlp()