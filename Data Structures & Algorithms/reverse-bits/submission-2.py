class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0

        for i in range(32):
            bit = 1 & (n>>i)
            ans += bit << (31 - i)

        return ans