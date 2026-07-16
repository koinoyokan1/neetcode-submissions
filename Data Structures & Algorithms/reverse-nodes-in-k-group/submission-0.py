# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node = head
        tail = None
        ans = None

        def rev(node):
            p = node
            for _ in range(k-1):
                if not p.next: return node, p, None
                p = p.next
            
            last = node
            prev, curr = None, node
            for _ in range(k):
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            return prev, last, curr

        while node:
            first, last, nxt = rev(node)
            if not ans: 
                ans = first
            else: 
                tail.next = first

            tail = last
            node = nxt

        return ans
