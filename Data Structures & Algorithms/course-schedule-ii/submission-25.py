from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        visited = set()
        cycle = False
        graph = defaultdict(list)

        for p in prerequisites:
            graph[p[0]].append(p[1])
        
        def dfs(start, visiting):
            if start in visited: return
            nonlocal cycle
            if cycle: return
            for n in graph[start]:
                if n in visiting:
                    cycle = True
                    return
                if n not in visited: dfs(n, visiting.union([n]))
            visited.add(start)
            ans.append(start)
        
        for i in range(numCourses):
            if cycle: return []
            if i not in visited: dfs(i, set([i]))
        
        if cycle: return []
        return ans