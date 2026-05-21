class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodeMap = {}

        if not node: return None

        visited = set()
        def dfs(start):
            if start in visited: return
            visited.add(start)
            if not start in nodeMap: nodeMap[start] = Node(start.val)
            for nei in start.neighbors:
                if not nei in nodeMap: nodeMap[nei] = Node(nei.val)
                nodeMap[start].neighbors.append(nodeMap[nei])
            for nei in start.neighbors: dfs(nei)

        dfs(node)

        return nodeMap[node]