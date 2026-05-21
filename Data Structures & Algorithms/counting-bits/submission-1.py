class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for num in range(n+1):
            one = 0

            while num:
                num = num & (num - 1)
                one += 1
            res.append(one)
        
        return res