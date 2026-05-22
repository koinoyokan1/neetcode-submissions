# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        if not root.left and not root.right: return root

        stack = [root]
        while stack:
            p = stack.pop()
            p.left, p.right = p.right, p.left
            if p.left: stack.append(p.left)
            if p.right: stack.append(p.right)
        return root