# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        stack =[]
        p = root
        while p:
            stack.append(p)
            p = p.left
        
        ans = []
        while stack:
            p = stack.pop()
            ans.append(p.val)
            if p.right:
                p = p.right
                while p:
                    stack.append(p)
                    p = p.left
        
        return ans[k-1]