class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        charSet = {}
        maxLen = 0

        for start in range(len(s)):
            while end < len(s) and s[end] not in charSet:
                maxLen = max(end - start + 1, maxLen)
                charSet[s[end]] = end
                end += 1

            # if end == len(s): return max(end - start, maxLen)
            del charSet[s[start]]
        
        return maxLen
        
