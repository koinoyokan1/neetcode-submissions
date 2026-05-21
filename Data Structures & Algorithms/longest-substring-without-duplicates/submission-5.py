class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        cntr = defaultdict(int)

        mxLen = 0
        for right in range(len(s)):
            cntr[s[right]] += 1
            while cntr[s[right]] > 1:
                cntr[s[left]] -= 1
                left += 1

            mxLen = max(mxLen, right - left + 1)
        
        return mxLen
            
