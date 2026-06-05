from functools import lru_cache

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        @lru_cache(maxsize=None)
        def cR(i=0):
            print(i)
            if i >= len(s): return False
            if s[i] != '0': return False
            if i == len(s) - 1: return True

            for j in range(maxJump, minJump-1,-1):
                if cR(i+j): 
                    print(i, 'True')
                    return True

            print(i, 'False')

            return False

        return cR()