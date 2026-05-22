class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for t in times:
            graph[t[0]].append((t[1], t[2]))
        distance = [math.inf for _ in range(n+1)] 
        distance[0] = 0
        distance[k] = 0
        heap = [(0, k)]
        while heap:
            dst, v = heapq.heappop(heap)
            for nei, dx in graph[v]:
                newDst = dst + dx
                if newDst < distance[nei]:
                    distance[nei] = newDst
                    heapq.heappush(heap, (newDst, nei))
        print(distance)
        if math.inf in distance: return -1
        return max(distance)