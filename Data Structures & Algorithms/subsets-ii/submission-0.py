class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        numsCntr = Counter(nums)
        nums = list(numsCntr.keys())

        def _hlp(i=0, currAns=[]):
            if i == len(nums): return [currAns]

            ans = []
            for j in range(numsCntr[nums[i]]+1):
                ans.extend(_hlp(i+1, currAns + [nums[i]]*j))
            
            return ans
        return _hlp()
