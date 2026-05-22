# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
             1
                    2
                 3     4
                   5    6
'''
from functools import lru_cache

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        @lru_cache()
        def ht(node):
            if not node: return 0
            if not node.left and not node.right: return 1
            return max(ht(node.left), ht(node.right)) + 1
        print(ht(root))
        mxDiameter = 0
        stack = [root]
        while stack:
            n = stack.pop()
            if not n: continue
            mxDiameter = max(mxDiameter, ht(n.left) + ht(n.right), ht(n.left), ht(n.right))
            stack.append(n.left)
            stack.append(n.right)

        return mxDiameter