# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, -math.inf, math.inf)]

        while stack:
            node, mn, mx = stack.pop()
            if not mn <= node.val <= mx: return False
            if node.left: stack.append((node.left, mn, node.val-1)) 
            if node.right: stack.append((node.right, node.val+1, mx))

        return True 
