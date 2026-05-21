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
        toVisit = set([i for i in range(n)])
        res = 0

        while len(toVisit) > 0:
            cost, i = heapq.heappop(heap)
            if i not in toVisit: continue
            toVisit.remove(i)
            res += cost
            for nei, dst in graph[i]:
                heapq.heappush(heap, (dst, nei))

        return res

