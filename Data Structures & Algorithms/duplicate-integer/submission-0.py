class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numDict = set()

        for num in nums:
            if num not in numDict:
                numDict.add(num)
            else:
                return True
        
        return False
         