'''
0101
0110
0111
1000
1001
1010
'''
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        cnt = 0
        while left != right:
            left  >>= 1
            right >>= 1
            cnt += 1
        left <<= cnt
        return left