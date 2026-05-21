# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        iter = root

        while iter:
            if p.val < iter.val and q.val < iter.val:
                iter = iter.left
            elif p.val > iter.val and q.val > iter.val:
                iter = iter.right
            else:
                return iter

        return None