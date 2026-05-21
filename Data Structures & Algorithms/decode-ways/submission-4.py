from functools import lru_cache
class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache(maxsize=None)
        def _hlp(i=0):   
            # if i > len(s): return 0
            if i == len(s): return 1
            if s[i] == '0': return 0     

            ans = _hlp(i+1)
            if i == len(s) - 1:return ans
            if s[i] not in ['1','2'] or (s[i] == '2' and s[i+1] in ['7','8','9']): return ans
            return ans + _hlp(i+2)

        return _hlp()
    