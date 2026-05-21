class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums) - 1

        numsDict = {}

        for i in range(len(nums)):
            if target - nums[i] in numsDict:
                return [numsDict[target - nums[i]], i]
            numsDict[nums[i]] = i

