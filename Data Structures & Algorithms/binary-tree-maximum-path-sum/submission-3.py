# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        mxPathSum = root.val

        def _maxPathSum(node):
            nonlocal mxPathSum
            if not node: return 0
            if not node.left and not node.right: 
                mxPathSum = max(mxPathSum, node.val)
                return node.val

            mxHtAddLeft = mxHtAddRight = 0
            mxPathSumLeft = mxPathSumRight = float("-inf")
            if node.left:
                mxHtAddLeft = _maxPathSum(node.left)
            if node.right:
                mxHtAddRight = _maxPathSum(node.right)

            mxHtAdd = node.val + max(mxHtAddLeft, mxHtAddRight, 0)
            mxPathSum = max(mxPathSum, node.val + max(mxHtAddLeft, 0) + max(0, mxHtAddRight))

            return mxHtAdd
        
        _maxPathSum(root)
        return mxPathSum