from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letterCnt = defaultdict(int)
        
        for ltr in s:
            letterCnt[ltr] += 1
        
        for ltr in t:
            if letterCnt[ltr] == 0: return False
            letterCnt[ltr] -= 1
        
        for ltr in set(s):
            if letterCnt[ltr] != 0:
                return False

        return True