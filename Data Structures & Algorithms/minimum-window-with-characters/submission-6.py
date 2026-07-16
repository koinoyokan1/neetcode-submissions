class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        ans = [0, len(s)]

        tCntr = Counter(t)

        for right in range(len(s)):
            tCntr[s[right]] -= 1
            while all(v <= 0 for v in tCntr.values()):
                if right - left < ans[1] - ans[0]:
                    ans[0], ans[1] = left, right
                tCntr[s[left]] += 1
                left += 1

        if ans == [0, len(s)]: return ""
        return s[ans[0]:ans[1]+1]