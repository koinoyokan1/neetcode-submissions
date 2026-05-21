class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        cntr = defaultdict(int)

        mxLen = 0

        def invalidWindow():
            replacementNeeded = sum(cntr.values()) - max(cntr.values())
            return replacementNeeded > k

        for right in range(len(s)):
            cntr[s[right]] += 1
            while left <= right and invalidWindow():
                cntr[s[left]] -= 1
                left += 1
            
            mxLen = max(mxLen, right - left + 1)
        
        return mxLen