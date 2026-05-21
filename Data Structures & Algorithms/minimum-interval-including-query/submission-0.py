class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        ans = [0] * len(queries)
        queries = [(queries[i], i) for i in range(len(queries))]
        queries.sort()

        heap = []
        j = 0
        for q, qindex in queries:
            while j < len(intervals):
                i = intervals[j]
                if i[0] > q: break
                heapq.heappush(heap, (i[1]-i[0]+1, j))
                j += 1

            while heap:
                dst, index = heap[0]
                if intervals[index][1] < q: 
                    heapq.heappop(heap)
                else:
                    break

            if heap: ans[qindex] = heap[0][0]
            else: ans[qindex] = -1
        return ans