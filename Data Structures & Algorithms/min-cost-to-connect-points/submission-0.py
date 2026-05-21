class Graph:
    def __init__(self, edges):
        self.graph = defaultdict(list)
        self.n = len(edges)

        for i in range(self.n-1):
            for j in range(i+1, self.n):
                cost = abs(edges[j][1] - edges[i][1]) + abs(edges[j][0] - edges[i][0])           
                self.graph[i].append((cost, j))
                self.graph[j].append((cost, i))

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        g = Graph(points)

        heap = [(0, 0)]

        ans = 0
        while len(visited) < g.n:
            dist, node = heapq.heappop(heap)
            if node in visited: continue
            visited.add(node)
            ans += dist
            for dst2, nei in g.graph[node]:
                heapq.heappush(heap, (dst2, nei))
        
        return ans