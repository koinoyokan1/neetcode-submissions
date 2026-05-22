# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0

        p = root
        stack = [root]
        while p.left: 
            stack.append(p.left)
            p = p.left

        while stack:
            p = stack.pop()
            cnt += 1
            if k == cnt: return p.val
            if p.right:
                p = p.right
                stack.append(p)
                while p.left: 
                    stack.append(p.left)
                    p = p.left
                