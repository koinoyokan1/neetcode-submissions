# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []

        def _prefix(curr):
            if not curr: return
            _prefix(curr.left)
            ans.append(curr.val)
            _prefix(curr.right)

        _prefix(root)
        return ans[k-1]
        