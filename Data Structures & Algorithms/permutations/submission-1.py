class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def _hlp(currAns=[], remSet=set(nums)):
            if len(remSet) == 0: return [currAns]

            ans = []
            for num in remSet:
                ans.extend(_hlp(currAns + [num], remSet - {num}))
            
            return ans
        
        return _hlp()
