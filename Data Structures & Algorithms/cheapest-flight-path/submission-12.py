class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [math.inf] * n
        prices[src] = 0

        for _ in range(k+1):
            prevprices = prices.copy()
            for s, d, p in flights:
                prevprices[d] = min(prices[s] + p, prevprices[d])
            prices = prevprices.copy()
            
        if prices[dst] == math.inf: return -1
        return prices[dst]
