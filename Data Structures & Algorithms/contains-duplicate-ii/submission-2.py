# 1,2,3,1 
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        present = defaultdict(set)
        l = 0

        for r in range(len(nums)):
            while r - l > k:
                present[nums[l]].remove(l)
                l += 1

            if len(present[nums[r]]) > 0: return True
            present[nums[r]].add(r)

        return False




