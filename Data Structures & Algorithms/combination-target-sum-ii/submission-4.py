class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        numsCnt = Counter(nums)
        nums = list(set(nums))


        def _combinationSum2(target=target, i=0, comb=[]):
            if target == 0: return [comb]

            ans = []
            for j in range(i, len(nums)):
                for m in range(1, numsCnt[nums[j]]+1):
                    c = m*[nums[j]]

                    if target-sum(c) < 0: break
                    ans.extend(_combinationSum2(target-sum(c), j+1, comb + c))

            return ans
        
        return _combinationSum2()