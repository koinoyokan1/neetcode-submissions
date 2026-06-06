class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cand = nums[0]
        cnt = 1

        for n in nums[1:]:
            if cnt == -1:
                cnt = 0
                cand = n
            if n == cand:
                cnt += 1
            else:
                cnt -= 1
        
        return cand