# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []

        def _preOrder(node):
            if node.left: _preOrder(node.left)

            ans.append(node.val)
            if node.right: _preOrder(node.right)
        
        
        _preOrder(root)
        print(ans)
        return ans[k-1]