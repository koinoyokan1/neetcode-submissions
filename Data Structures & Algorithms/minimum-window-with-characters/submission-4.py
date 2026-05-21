class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        tCntr = Counter(t)

        def validWindow():
            for k in set(t):
                if tCntr[k] > 0: return False
            return True

        minL, minR = -1, len(s)
        for right in range(len(s)):
            tCntr[s[right]] -= 1
            while left <= right and validWindow():
                if right - left <= minR - minL:
                    minL, minR = left, right 
                tCntr[s[left]] += 1                
                left += 1
        
        if minL == -1: return ""
        return s[minL:minR+1]