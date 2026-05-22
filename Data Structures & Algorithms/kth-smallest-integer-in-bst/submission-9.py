# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []

        p = root
        stack = [root]
        while p.left: 
            stack.append(p.left)
            p = p.left

        while stack:
            p = stack.pop()
            ans.append(p.val)
            if len(ans) == k: return ans[-1]
            if p.right:
                p = p.right
                stack.append(p)
                while p.left: 
                    stack.append(p.left)
                    p = p.left
        return ans[-1]
                