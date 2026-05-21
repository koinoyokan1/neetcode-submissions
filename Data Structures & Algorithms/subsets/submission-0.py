class Solution:

        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def _subsets(i=0, ans=[]):
            if i == len(nums): return [ans]

            a = []
            a = _subsets(i+1, ans + [nums[i]])
            a.extend(_subsets(i+1, ans))
            return a
        return _subsets()