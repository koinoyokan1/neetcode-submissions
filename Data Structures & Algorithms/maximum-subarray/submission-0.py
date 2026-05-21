class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = max(nums)
        if m < 0: return m
        
        mx = 0

        currSum = 0 
        for num in nums:
            currSum += num
            if currSum < 0: currSum = 0
            mx = max(mx, currSum) 
        
        return mx