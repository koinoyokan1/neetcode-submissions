class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodeMap = {}

        if not node: return None
        copyNode = Node(node.val)
        nodeMap[node] = copyNode

        visited = set()
        def dfs(start, visiting):
            if start in visited: return
            for nei in start.neighbors:
                if not nei in nodeMap: 
                    nodeMap[nei] = Node(nei.val)
                nodeMap[start].neighbors.append(nodeMap[nei])
                if nei in visiting: continue

                visiting.add(nei)
                dfs(nei, visiting)
                visiting.remove(nei)           
            visited.add(start)

        dfs(node, set([node]))

        return copyNode