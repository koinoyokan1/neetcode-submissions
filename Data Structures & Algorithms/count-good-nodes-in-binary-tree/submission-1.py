# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return None

        stack = [(root, root.val)]
        ans = 1

        while stack:
            node, currMax = stack.pop()
            if node.right:
                if node.right.val >= currMax: ans += 1
                stack.append((node.right, max(node.right.val, currMax)))
            if node.left: 
                if node.left.val >= currMax: ans += 1
                stack.append((node.left, max(node.left.val, currMax)))
        
        return ans
