class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        least = 101

        maxProfit = 0
        for price in prices:
            maxProfit = max(maxProfit, price - least)
            least = min(least, price)
            
        return maxProfit