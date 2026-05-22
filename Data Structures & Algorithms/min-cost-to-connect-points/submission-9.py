class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = [(0, points[0][0], points[0][1])]
        visited = set()
        distance = 0
        while heap:
            dst, x, y = heapq.heappop(heap)
            if (x, y) in visited: continue
            visited.add((x, y))
            print(x, y, dst)
            distance += dst

            for point in points:
                if (point[0], point[1]) in visited: continue
                heapq.heappush(heap, (abs(point[0]-x) + abs(point[1]-y), point[0], point[1]))

        return distance