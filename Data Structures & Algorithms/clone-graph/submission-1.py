"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        map = {}
        copyHead = Node(node.val)
        map[node] = copyHead

        stack = [(node, copyHead)]
        visited = set()

        while stack:
            node, copy = stack.pop()
            if node in visited: continue
            visited.add(node)

            for nei in node.neighbors:
                if nei in map:
                    neicopy = map[nei]
                else:
                    neicopy = Node(nei.val)
                    map[nei] = neicopy
                copy.neighbors.append(neicopy)
                stack.append((nei, neicopy))
            
        return copyHead