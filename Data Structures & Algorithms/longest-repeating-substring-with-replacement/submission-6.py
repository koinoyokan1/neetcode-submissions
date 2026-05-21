class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        usedChrCnt = defaultdict(int)

        def isInvalidWindow():
            replacementsNeeded = sum(usedChrCnt.values()) - max(usedChrCnt.values()) 
            if replacementsNeeded > k: return True
            return False

        mxLen = 0
        for right in range(len(s)):
            usedChrCnt[s[right]] += 1
            while isInvalidWindow():
                usedChrCnt[s[left]] -= 1
                left += 1

            print(left, right, usedChrCnt)
            mxLen = max(mxLen, right - left + 1)
        
        return mxLen