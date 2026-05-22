class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0

        ans = 1
        stack = [(root, root.val)]

        while stack:
            n, mx = stack.pop()

            if n.left:
                if n.left.val >= mx: 
                    print(mx, n.left.val)
                    ans += 1
                stack.append((n.left, max(n.val, n.left.val, mx)))

            if n.right:
                if n.right.val >= mx: 
                    print(mx, n.right.val)                    
                    ans += 1
                stack.append((n.right, max(n.val, n.right.val, mx)))

        return ans
