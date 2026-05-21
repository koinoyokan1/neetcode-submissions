class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths are not equal then strings cannot be anagrams
        if len(s) != len(t): return False

        cntS, cntT = {}, {}

        for i in range(len(s)):
            cntS[s[i]] = cntS.get(s[i], 0) + 1
            cntT[t[i]] = cntT.get(t[i], 0) + 1
        
        return cntS == cntT
