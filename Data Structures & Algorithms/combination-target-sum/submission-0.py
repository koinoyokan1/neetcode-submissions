class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def _combinationSum(i=0, target=target, comb=[]):
            if target == 0: return [comb]

            ans = []
            for j in range(i, len(nums)):
                if target - nums[j] >= 0:
                    ans.extend(_combinationSum(j,target-nums[j], comb + [nums[j]]))
            
            return ans
        
        return _combinationSum()

