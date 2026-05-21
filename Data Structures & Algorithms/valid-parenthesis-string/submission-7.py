class Solution:
    def __init__(self):
        self.validStringCache = {}

    def _checkvalidStringHelperCache(self, st: str, st_i: int=0, openCnt: int=0) -> bool:
        if (st_i, openCnt) in self.validStringCache:
            return self.validStringCache[(st_i, openCnt)]
        
        res = self._checkValidString(st, st_i, openCnt)
        self.validStringCache[(st_i, openCnt)] = res

        return res

    def _checkValidString(self, s, i=0, cnt=0):
        if i == len(s): return cnt == 0
        if s[i] == '(':
            if self._checkvalidStringHelperCache(s, i+1, cnt+1): return True
        elif s[i] == ')':
            if cnt > 0 and self._checkvalidStringHelperCache(s, i+1, cnt-1): return True
        else:
            if self._checkvalidStringHelperCache(s, i+1, cnt): return True
            if self._checkvalidStringHelperCache(s, i+1, cnt+1): return True
            if cnt > 0 and self._checkvalidStringHelperCache(s, i+1, cnt-1): return True
        return False

    def checkValidString(self, s: str) -> bool:
        return self._checkvalidStringHelperCache(s)