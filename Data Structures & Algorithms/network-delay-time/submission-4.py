class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for t in times:
            graph[t[0]].append((t[1], t[2]))
            
        distance = [math.inf for _ in range(n+1)] 
        distance[0] = 0
        distance[k] = 0
        heap = [(0, k)]
        visited = set()

        while heap:
            d, n = heapq.heappop(heap)
            if n in visited: continue
            visited.add(n)
            distance[n] = d
            for nei, ed in graph[n]:
                if nei in visited: continue
                heapq.heappush(heap, (ed+d, nei))

        if math.inf in distance: return -1
        return max(distance)