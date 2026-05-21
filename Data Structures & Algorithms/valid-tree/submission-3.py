class Solution:
    def validTree(self, num: int, edges: List[List[int]]) -> bool:
        if num == 0: return None

        graph = defaultdict(list)

        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])

        visited = set()

        stack = [(0, {0}, -1)]
        while stack:
            n, visiting, parent = stack.pop()
            if n in visited: continue
            visited.add(n)
            for nei in graph[n]:
                if nei == parent: continue
                if nei in visiting: return False
                stack.append((nei, visiting.union({nei}), n))
        
        return len(visited) == num