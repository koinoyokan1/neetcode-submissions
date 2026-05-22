class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ans = [-1, -1, -1]
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]: continue
            ans = [max(ans[0], t[0]), max(ans[1], t[1]), max(ans[2], t[2])]
        
        return target == ans