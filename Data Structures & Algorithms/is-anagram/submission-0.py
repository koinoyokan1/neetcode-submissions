class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        chrCnt = Counter(s)

        for c in t:
            if chrCnt[c] == 0: return False
            chrCnt[c] -= 1
        
        return True