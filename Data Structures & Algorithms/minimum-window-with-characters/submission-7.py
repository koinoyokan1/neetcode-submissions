class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        ans = [0, len(s)]
        tset = set(t)
        missing = set(t)
        tCntr = Counter(t)

        for right in range(len(s)):
            tCntr[s[right]] -= 1
            if tCntr[s[right]] == 0: missing.remove(s[right]) 
            while not missing:
                if right - left < ans[1] - ans[0]:
                    ans[0], ans[1] = left, right
                tCntr[s[left]] += 1
                if tCntr[s[left]] > 0: missing.add(s[left])
                left += 1

        if ans == [0, len(s)]: return ""
        return s[ans[0]:ans[1]+1]