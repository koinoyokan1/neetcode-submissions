class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [math.inf for _ in range(n)]
        prices[src] = 0
        for _ in range(k+1):
            prevPrices = prices.copy()
            for s, d, p in flights:
                prices[d] = min(prices[d], prevPrices[s] + p)
            
        if prices[dst] == math.inf: return -1
        return prices[dst]