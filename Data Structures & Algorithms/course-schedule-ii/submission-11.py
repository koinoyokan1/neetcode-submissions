class Solution:
    def __init__(self):
        self.cycle = False
        ans = []

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for p in prerequisites:
            graph[p[1]].append(p[0])

        visited = set()
        ans = []

        def dfs(start, visiting):
            if self.cycle: return
            if start in visited: return
            for nei in graph[start]:
                if nei in visiting: 
                    self.cycle = True
                    return
                visiting.add(nei)
                dfs (nei, visiting)
                if self.cycle: return

                visiting.remove(nei)
            visited.add(start)

            ans.append(start)

        for i in range(numCourses):
            if self.cycle: 
                print(self.cycle)
                return []
            if i in visited: continue
            dfs(i, set([i]))
        
        if self.cycle: return []
        return ans[::-1]
