'''
c = 1
netProfit = [(1,-3),(1,-1)]
tmp = [(2,-1)]
'''
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap = []

        for i in range(len(profits)):
            np = profits[i]
            heapq.heappush(heap, (-np, i))
        found = False
        for i in range(k):
            tmp = []
            while heap:
                np, pi = heapq.heappop(heap)
                if capital[pi] > w:
                    tmp.append((np, pi))
                    continue
                w += profits[pi]
                found = True
                break
            if not found: break
            while tmp:
                heapq.heappush(heap, (tmp.pop()))
        
        return w
