# 1, 2, 4, 6
# 1, 1, 2, 8
# 48, 24, 6, 1
# 48, 24, 12, 8
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixMulti, suffixMulti, ans = [1] * len(nums), [1] * len(nums), [1] * len(nums)

        for prefixIndex in range(1, len(nums)):
            suffixIndex = len(nums) - prefixIndex - 1
            prefixMulti[prefixIndex] = prefixMulti[prefixIndex-1] * nums[prefixIndex-1]
            suffixMulti[suffixIndex] = suffixMulti[suffixIndex+1] * nums[suffixIndex+1]
        
        print(prefixMulti, suffixMulti)
        for i in range(len(nums)):
            ans[i] = suffixMulti[i]*prefixMulti[i]
        
        return ans