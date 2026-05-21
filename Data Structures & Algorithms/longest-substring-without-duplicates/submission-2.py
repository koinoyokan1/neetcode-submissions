class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        charSet = defaultdict(int)
        maxLen = 0

        for end in range(len(s)):
            charSet[s[end]] += 1

            while charSet[s[end]] > 1:
                charSet[s[start]] -= 1
                start += 1

            maxLen = max(end - start + 1, maxLen)

        return maxLen
        
