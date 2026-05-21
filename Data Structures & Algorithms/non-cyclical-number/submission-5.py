class Solution:
    def _subOfSquaresOfDigits(self, n):
        ans = 0
        while n:
            digit = n % 10
            ans += digit*digit
            n = (n-digit) // 10
        return ans

    def _isHappy(self, n, seen):
        if n == 1: return True
        newN = self._subOfSquaresOfDigits(n)
        if newN in seen: return False
        seen.add(newN)
        return self._isHappy(newN, seen)

    def isHappy(self, n: int) -> bool:
        return self._isHappy(n, set())
