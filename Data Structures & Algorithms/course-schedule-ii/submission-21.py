from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visiting = set()
        visited = set()
        cycle = False
        ans = []
        graph = defaultdict(list)
        
        for p in prerequisites:
            graph[p[0]].append(p[1])

        def dfs(start, visiting):
            nonlocal cycle
            if cycle: return

            for nei in graph[start]:
                if nei in visiting:
                    cycle = True
                    return
                visiting.add(nei)
                if nei in visited: continue
                dfs(nei, visiting)
                visiting.remove(nei)
            
            visited.add(start)
            ans.append(start)            

        for i in range(numCourses):
            if i in visited: continue
            dfs(i, set([i]))
            if cycle: return []
        
        if not cycle: return ans