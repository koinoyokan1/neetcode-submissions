import math

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [math.inf] * n
        prices[src] = 0

        for i in range(k+1):
            prevPrices = prices.copy()

            for s, d, p in flights:
                prevPrices[d] = min(prevPrices[d], prices[s] + p)
            
            prices = prevPrices
        
        if prices[dst] == math.inf: return -1
        return prices[dst]