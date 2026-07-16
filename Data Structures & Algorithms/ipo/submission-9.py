class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        accessible = []
        notAccessible = []

        for i in range(len(profits)):
            if capital[i] <= w:
                accessible.append(-profits[i])
            else:
                notAccessible.append((capital[i], i))

        heapq.heapify(accessible)
        heapq.heapify(notAccessible)

        capital = w
        for _ in range(k):
            if not accessible: return capital

            profit = heapq.heappop(accessible)
            profit = -profit
            capital += profit

            while notAccessible and notAccessible[0][0] <= capital:
                _, i = heapq.heappop(notAccessible)
                heapq.heappush(accessible, -profits[i])
            
        return capital


