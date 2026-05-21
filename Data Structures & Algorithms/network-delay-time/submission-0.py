class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for time in times:
            graph[time[0]].append((time[1], time[2]))

        
        heap = [(0, k)]
        toVisit = set([i for i in range(1, n+1)])
        mxTime = 0

        while heap:
            time, node = heapq.heappop(heap)
            if node not in toVisit: continue
            toVisit.remove(node)
            mxTime = max(mxTime, time)
            for nei, dst in graph[node]:
                heapq.heappush(heap, (time + dst, nei))
        
        if len(toVisit) == 0: return mxTime
        return -1
        