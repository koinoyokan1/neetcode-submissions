# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        n = root

        while n:
            if q.val < p.val: p, q = q, p
            if p.val <= n.val <= q.val: return n
            if p.val < n.val: 
                n = n.left
            else:
                n = n.right
