class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for p in prerequisites:
            graph[p[1]].append(p[0])

        visited = set()
        stack = []
        cycle = False

        def topoSort(i, visiting):
            nonlocal cycle, stack
            if cycle: return
            visited.add(i)
            for nei in graph[i]:
                # if nei in visited: continue
                if nei in visiting: 
                    cycle = True
                    return
                topoSort(nei, visiting.union({nei}))
            stack.append(i)

        for i in range(numCourses):
            if i in visited: continue
            if cycle: return []
            topoSort(i, {i})
        
        if not cycle: return stack[::-1]
        return []

        