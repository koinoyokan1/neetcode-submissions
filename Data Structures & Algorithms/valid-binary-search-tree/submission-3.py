# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def _isValidBST(node, mn=-math.inf, mx=math.inf):
            if not node: return True
            if not mn <= node.val <= mx: return False
            return _isValidBST(node.left, mn, node.val-1) and _isValidBST(node.right, node.val+1, mx)

        return _isValidBST(root)