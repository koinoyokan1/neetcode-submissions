# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        queue = deque([(root, -1001, 1001)])

        while queue:
            node, mn, mx = queue.popleft()
            if node.val >= mx: return False
            if node.val <= mn: return False
            if node.left: queue.append((node.left, mn, node.val))
            if node.right: queue.append((node.right, node.val, mx))
        
        return True
