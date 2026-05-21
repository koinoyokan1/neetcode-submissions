class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minTillNow = 1
        maxTillNow = 1
        res = max(nums)

        for num in nums:
            if num == 0:
                minTillNow = 1
                maxTillNow = 1
                continue

            tmp = maxTillNow * num
            maxTillNow = max(num, minTillNow * num, maxTillNow * num)
            minTillNow = min(num, minTillNow * num, tmp)
            res = max(res, maxTillNow)
        return res

