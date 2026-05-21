# 2^1
# 2^1
class Solution:
    def myPowPos(self, x, n):
        if n == 0: return 1
        
        ans = self.myPow(x, int(n/2))
        res = 0

        if n % 2 == 0:
            res = ans * ans
        else:
            res = ans * ans * x

        return res

    def myPow(self, x: float, n: int) -> float:
        ans = self.myPowPos(x, abs(n))
        if n < 0: return 1/ans
        return ans