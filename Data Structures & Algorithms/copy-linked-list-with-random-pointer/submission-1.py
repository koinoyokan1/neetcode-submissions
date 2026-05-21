"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None

        p = head
        q = None
        qhead = None
        nodeMap = {}

        while p:
            if not qhead: 
                qhead = Node(p.val)
                q = qhead
                p = p.next
                nodeMap[head] = qhead
                continue
            q.next = Node(p.val)
            q = q.next
            nodeMap[p] = q

            p = p.next

        p = head
        q = qhead

        while p:
            if p.random:
                q.random = nodeMap[p.random]
            p = p.next
            q = q.next
        
        return qhead
