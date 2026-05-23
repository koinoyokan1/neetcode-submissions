from functools import lru_cache

class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache        
        def _hlp(i=0):
            if i == len(s): return True

            for w in wordDict:
                if s[i:].startswith(w):
                    if _hlp(i+len(w)): return True
            return False

        return _hlp()
