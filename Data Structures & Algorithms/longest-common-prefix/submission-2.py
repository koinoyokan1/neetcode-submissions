class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if "" in strs: return ""
        ans = strs[0]
        for s in strs[1:]:
            print(len(ans), len(s))

            for i in range(min(len(ans), len(s))):
                print(ans[i]==s[i])
                if ans[i] != s[i]: break
            else:
                i += 1
            ans = ans[:i]
            print(i, ans)
        
        return ans

