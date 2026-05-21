class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        
        def validWindow(left, right):
            st = s[left:right+1]
            cntr = Counter(st)
            return len(st) == len(list(cntr.keys()))

        mxLen = 0
        for right in range(len(s)):
            while left < right and not validWindow(left, right):
                left += 1
            if left > right: continue

            mxLen = max(mxLen, right - left + 1)
        
        return mxLen
            
