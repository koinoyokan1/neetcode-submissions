class Solution:
    def __init__(self):
        self.ans = {}

    def _minCostClimbingStairs(self, cost, i=0):
        if i in self.ans: return self.ans[i]
        if i == len(cost): return 0
        if i > len(cost): return sys.maxsize

        a = cost[i] + min(self._minCostClimbingStairs(cost, i+1), self._minCostClimbingStairs(cost, i+2))
        self.ans[i] = a
        return a

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return min(self._minCostClimbingStairs(cost, 0), self._minCostClimbingStairs(cost, 1))