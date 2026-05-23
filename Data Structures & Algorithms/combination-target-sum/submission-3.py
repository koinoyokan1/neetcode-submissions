class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        def _cb(i=0, comb=[], target=target):
            if target == 0: return [comb]

            ans = []
            for j in range(i, len(nums)):
                if target - nums[j] < 0: break
                ans.extend(_cb(j, comb + [nums[j]], target - nums[j]))
            
            return ans
        
        return _cb()

