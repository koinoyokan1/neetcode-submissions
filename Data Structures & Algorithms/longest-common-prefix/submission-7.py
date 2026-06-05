class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        ans = strs[0]
        for i in range(len(strs[0])):
            for s in strs:
                if len(s) <= i or len(ans) <= i or ans[i] != s[i]: return ans[:i]
        return ans                

