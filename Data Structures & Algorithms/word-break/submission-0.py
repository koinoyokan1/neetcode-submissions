from functools import lru_cache

class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache        
        def _hlp(i=0):
            if i == len(s): return True
            if i > len(s): return False

            for word in wordDict:
                subStringOfS = s[i:i+len(word)]
                if subStringOfS == word and _hlp(i+len(word)): return True
            return False

        return _hlp()
