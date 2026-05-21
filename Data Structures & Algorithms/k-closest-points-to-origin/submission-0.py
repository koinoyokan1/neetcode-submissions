import heapq

class Solution:
    def calcDistanceFromCenter(self, point):
        return point[0]*point[0] + point[1]*point[1]

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            dst = self.calcDistanceFromCenter(point)
            heapq.heappush(heap, (-dst, point))
            if len(heap) > k:
                heapq.heappop(heap)

        ans = [point for dst, point in heap]
        return ans
