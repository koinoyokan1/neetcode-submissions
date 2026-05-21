# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        m1 = self.maxHeight(root.left) + self.maxHeight(root.right)
        m2 = self.diameterOfBinaryTree(root.left) 
        m3 = self.diameterOfBinaryTree(root.right) 

        return max(m1, m2, m3)