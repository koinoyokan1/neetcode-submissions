class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def _p(i=0, comb=[]):
            if i == len(nums):
                return [comb]
            
            ans = []
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                ans.extend(_p(i + 1, nums.copy())) 
                nums[i], nums[j] = nums[j], nums[i]
            return ans
        
        return _p()