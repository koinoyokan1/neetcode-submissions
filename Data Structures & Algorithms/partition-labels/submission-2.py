class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        l = 0
        ans = []

        mp = {}
        for i in range(len(s)):
            c = s[i]
            mp[c] = i
        
        left = 0
        mx = -1
        for i in range(len(s)):
            c = s[i]
            mx = max(mx, mp[c])
            if i == mx: 
                ans.append(i - left + 1)
                mx = i
                left = i + 1
        return ans