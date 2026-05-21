class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = 0
        multiplier = 1

        for d2str in num2[::-1]:
            innerMultiplier = multiplier
            for d1str in num1[::-1]:
                d1 = int(d1str)
                d2 = int(d2str)

                ans += d1*d2*innerMultiplier
                innerMultiplier *= 10
            multiplier *= 10
        return str(ans)