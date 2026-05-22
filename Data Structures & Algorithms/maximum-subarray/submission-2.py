class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mxSum = max(nums)
        currSum = 0
        for num in nums:
            if currSum + num < 0: currSum = 0
            else:
                currSum += num 
                mxSum = max(currSum, mxSum)
        
        return mxSum