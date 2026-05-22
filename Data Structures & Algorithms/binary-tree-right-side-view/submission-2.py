# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        queue = deque()

        if not root: return []
        queue.append((root, 1))

        while queue:
            n, level = queue.popleft()
            if len(ans) < level: ans.append(n.val)
            else: ans[level-1] = n.val
            if n.left: queue.append((n.left, level+1))
            if n.right: queue.append((n.right, level+1))

        return ans
