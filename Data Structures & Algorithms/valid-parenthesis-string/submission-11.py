from functools import lru_cache
class Solution:
    def checkValidString(self, s: str) -> bool:
        mxOpen = math.floor(len(s)/2.0)

        @lru_cache(maxsize=None)
        def _checkValid(start=0, currOpen=0):
            if not 0 <= currOpen <= mxOpen: return False

            for i in range(start, len(s)):
                c = s[i]
                if c == '(':
                    currOpen += 1
                    if currOpen > mxOpen: return False
                elif c == ')':
                    currOpen -= 1
                    if currOpen < 0: return False
                else:
                    return _checkValid(i+1, currOpen) or _checkValid(i+1, currOpen+1) or _checkValid(i+1, currOpen-1)
            return currOpen == 0

        return _checkValid()