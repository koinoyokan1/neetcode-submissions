class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cntr = Counter(nums)
        numMxLen = {}
        mxLen = 0

        for num in nums:
            ln = 1
            i = 1

            while cntr[num+i] > 0:
                if num+i in numMxLen:
                    ln = ln + numMxLen[num+i] 
                    break
                ln += 1
                i += 1

            numMxLen[num] = ln
            mxLen = max(mxLen, ln)
        
        return mxLen