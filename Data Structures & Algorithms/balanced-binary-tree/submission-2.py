# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.cache = {}
    def maxHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if root not in self.cache: self.cache[root] = 1 + max(self.maxHeight(root.left), self.maxHeight(root.right))
        return self.cache[root]

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        if abs(self.maxHeight(root.left) - self.maxHeight(root.right)) > 1: return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)