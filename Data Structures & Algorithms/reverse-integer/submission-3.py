class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0: 
            neg = True
            x = -x
        
        print(x)
        ans = 0
        while x:
            ans *= 10
            ans += x%10
            x = math.floor(x/10)

        if neg: ans = -ans
        print(ans)
        if -math.pow(2, 31) < ans < math.pow(2, 31) - 1: return ans
        return 0