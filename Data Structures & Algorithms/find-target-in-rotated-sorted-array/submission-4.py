class Solution:
    def findMid(self, nums):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right)//2

            if nums[mid] < nums[right]:
                right = mid
            else:
                left += 1
        return mid  

    def binSearch(self, nums, left, right, target):
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        mid = self.findMid(nums)

        ans = self.binSearch(nums, 0, mid-1, target)
        if ans != -1: return ans

        if mid >= len(nums): return -1

        return self.binSearch(nums, mid, len(nums)-1, target)
   