class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(points)

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                graph[i].append((j, dist))
                graph[j].append((i, dist))

        heap = [(0, 0)]
        visit = set()
        res = 0

        while len(visit) < n:
            cost, i = heapq.heappop(heap)
            if i in visit: continue
            visit.add(i)
            res += cost
            for nei, dst in graph[i]:
                heapq.heappush(heap, (dst, nei))

        return res

