class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        sc = Counter(s)
        tc = Counter(t)

        for ket in sc.keys():
            if sc[ket] == tc[ket]: continue
            else: return False
        
        return True

       
