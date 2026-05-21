class Solution:
    def _getIthBit(self, a, i):
        return (a >> i) & 1

    def getSum(self, a: int, b: int) -> int:
        carry = 0
        ans = 0

        for i in range(32):
            bit = self._getIthBit(a, i) ^ self._getIthBit(b, i) ^ carry 
            if self._getIthBit(a, i) + self._getIthBit(b, i) + carry > 1: carry = 1
            else: carry = 0
            if bit: ans |= (1 << i)
        
        if ans > 0x7FFFFFFF:
            ans = ~(ans ^ 0xFFFFFFFF)
        return ans