from functools import lru_cache

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        @lru_cache(maxsize=None)
        def height(node):
            if not node: return 0
            if not node.left and not node.right: return 1

            return max(height(node.left), height(node.right)) + 1

        def _isBalanced(node):
            if not node: return True
            return _isBalanced(node.left) and _isBalanced(node.right) and abs(height(node.left) - height(node.right)) <= 1

        return _isBalanced(root)