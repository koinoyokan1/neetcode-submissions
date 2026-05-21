class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        while x:
            ans *= 10
            ans += int(math.fmod(x, 10))
            x = int(x/10)

        if -math.pow(2, 31) < ans < math.pow(2, 31) - 1: return ans
        return 0