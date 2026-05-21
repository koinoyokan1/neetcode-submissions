class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = [(nums[i], i) for i in range(len(nums))]
        nums.sort()
        print(nums)
        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left][0] + nums[right][0] == target: return sorted([nums[left][1], nums[right][1]])
            if nums[left][0] + nums[right][0] < target: left += 1
            else: right -= 1
        
