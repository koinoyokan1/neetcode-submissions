# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head

        prev = None
        curr = head

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        def printLl(n):
            while n:
                print(n.val)
                n = n.next

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        rHead = self.reverseList(slow.next)
        slow.next = None  
        p, q = head, rHead
        while q:
            tmp1, tmp2 = p.next, q.next
            p.next = q
            q.next = tmp1
            p = tmp1
            q = tmp2
