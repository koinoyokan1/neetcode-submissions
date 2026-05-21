class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n+1)
        last2Power = 1

        for i in range(1, n+1):
            if last2Power * 2 == i:
                last2Power *= 2 

            res[i] = 1 + res[i - last2Power] 

        return res