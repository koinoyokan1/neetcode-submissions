from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        @lru_cache(maxsize=None)
        def mth(si=0, pi=0):
            
            if pi == len(p): return si == len(s)

            if pi < len(p)-1 and p[pi+1] == '*':
                if mth(si, pi+2): return True

                sii = si
                while sii < len(s) and (p[pi] == '.' or s[sii] == p[pi]):
                    sii += 1
                    if mth(sii, pi+2): return True
                return False

            if si == len(s): return False

            if p[pi] == '.' or s[si] == p[pi]: return mth(si+1, pi+1)

            return False

        return mth()