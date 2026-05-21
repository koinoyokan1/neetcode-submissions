class Solution:
    def checkValidString(self, s: str) -> bool:
        def _checkValidString(i=0, openParanthesis=0):
            if openParanthesis > len(s) - i: return False
            if i == len(s): return openParanthesis == 0
            if s[i] == '(':
                if _checkValidString(i+1, openParanthesis+1): return True
            elif s[i] == ')':
                if openParanthesis == 0: return False
                if _checkValidString(i+1, openParanthesis-1): return True
            else:
                if openParanthesis > 0 and _checkValidString(i+1, openParanthesis-1): return True
                if _checkValidString(i+1, openParanthesis+1): return True
                if _checkValidString(i+1, openParanthesis): return True

            return False

        return _checkValidString()
