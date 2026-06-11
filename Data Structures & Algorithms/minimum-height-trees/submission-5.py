class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if len(edges) == 0: return [n-1]
        g = defaultdict(set)

        for edge in edges:
            g[edge[0]].add(edge[1])
            g[edge[1]].add(edge[0])

        q = deque()

        for v in g.keys():
            if len(g[v]) == 1: 
                q.append(v)
        
        toRemove = n
        while toRemove > 2:
            qsize = len(q)
            for _ in range(qsize):
                v = q.popleft()
                for nei in g[v]:
                    g[nei].remove(v)
                    if len(g[nei]) == 1: q.append(nei)
            toRemove -= qsize
        
        return list(q)




