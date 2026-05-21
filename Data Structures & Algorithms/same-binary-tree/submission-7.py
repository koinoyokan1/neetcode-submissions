# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stackP, stackQ = [p], [q]

        while stackP and stackQ:
            ppop = stackP.pop()
            qpop = stackQ.pop()

            if ppop == None and qpop == None: continue
            if ppop == None or qpop == None: return False

            if ppop.val != qpop.val: return False

            stackP.append(ppop.left)
            stackQ.append(qpop.left)
            stackP.append(ppop.right)
            stackQ.append(qpop.right)

        if not stackP and not stackQ: return True
        return False

