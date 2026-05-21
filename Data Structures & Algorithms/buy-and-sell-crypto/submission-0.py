# 10 1 5 6 7 1
#  7 7 7 7 1 0

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxFuturePrice = [0] * len(prices)

        for i in range(len(prices) - 2, -1, -1):
            maxFuturePrice[i] = max(prices[i + 1], maxFuturePrice[i + 1])

        maxProfit = 0
        for i in range(len(prices) - 1):
            maxProfit = max(maxProfit, maxFuturePrice[i] - prices[i])
        
        return maxProfit