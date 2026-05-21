class Solution:
    def __init__(self):
        self.ans = {}

    def _climbStairs(self, n):
        if n in self.ans: return self.ans[n]
        if n == 0: return 1
        if n < 0: return 0

        a = self._climbStairs(n-1) + self._climbStairs(n-2)
        self.ans[n] = a
        return a

    def climbStairs(self, n: int) -> int:
        return self._climbStairs(n)