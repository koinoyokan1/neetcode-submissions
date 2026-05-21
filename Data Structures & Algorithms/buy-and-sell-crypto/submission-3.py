# 10 1 5 6 7 1
#  7 7 7 7 1 0

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currentMin = prices[0]
        maxProfit = 0

        for i in range(1, len(prices)):
            maxProfit = max(maxProfit, prices[i] - currentMin)
            currentMin = min(currentMin, prices[i])
        
        return maxProfit