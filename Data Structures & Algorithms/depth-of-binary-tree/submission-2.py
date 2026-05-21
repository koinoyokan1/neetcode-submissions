# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
            if not root: return 0

            maxD = 0
            stack = [(root, 1)]

            while stack:
                node, depth = stack.pop()
                if not node:
                    maxD = max(maxD, depth-1)
                    continue

                stack.append((node.left, depth+1))
                stack.append((node.right, depth+1))
            
            return maxD