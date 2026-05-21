class Solution:
    def twoSum(self, nums, start, target):
        ans = []
        j = len(nums) - 1
        i = start
        while i < j:
            if i != start and nums[i] == nums[i-1]: 
                i += 1
                continue
            
            if nums[i] + nums[j] == target:
                ans.append([nums[i], nums[j]])
                i += 1
                j -= 1
            elif nums[i] + nums[j] > target:
                j -= 1
            else:
                i += 1
        return ans

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        threeSums = []

        for i in range(len(nums)-2):
            if nums[i] > 0: break
            if i > 0 and nums[i] == nums[i-1]: continue

            twoSums = self.twoSum(nums, i+1, -nums[i])
            for twoSum in twoSums:
                threeSums.append([nums[i], twoSum[0], twoSum[1]])
            
        
        return threeSums