from collections import Counter
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cntr = Counter(nums)
        mxLen = 0
        crLn = 0
        ansDict = {}

        def dfs(start):
            if start in ansDict: return ansDict[start]

            if cntr[start + 1] == 0: 
                ansDict[start + 1] = 0
                return 1
            ans = dfs(start + 1) + 1
            ansDict[start] = ans
            print(start, ans)
            return ans

        for num in nums:
            mxLen = max(mxLen, dfs(num))
        
        return mxLen