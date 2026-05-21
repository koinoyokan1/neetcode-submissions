class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        start, end = 0, 0
        ans=  []
        lastChrPos = {}

        for i in range(len(s)):
            lastChrPos[s[i]] = i

        while start < len(s):
            i = start
            end = lastChrPos[s[start]]
            while i < end:
                end = max(lastChrPos[s[i]], end)
                i += 1
            ans.append(end-start+1)
            start = end + 1

        return ans
