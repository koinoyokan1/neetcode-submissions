# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        queue = deque()
        queue.append((root,0))
        
        ans = []
        while queue:
            node, level = queue.popleft()
            if len(ans) == level:
                ans.append(node.val)
            else:
                ans[level] = node.val
            if node.left: queue.append((node.left, level+1))
            if node.right: queue.append((node.right, level+1))
        
        return ans