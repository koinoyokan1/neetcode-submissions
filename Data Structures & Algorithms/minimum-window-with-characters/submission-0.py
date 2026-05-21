class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        tCntr = Counter(t)
        ans = ""

        def validWindow():
            for c in set(t):
                if tCntr[c] > 0: return False
            
            return True

        for right in range(len(s)):
            tCntr[s[right]] -= 1
            
            while validWindow():
                if ans == "" or len(ans) > right - left + 1:
                    ans = s[left:right+1]
                tCntr[s[left]] += 1
                left += 1    
        
        return ans