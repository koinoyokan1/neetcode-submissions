# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
n = 5
1 2 3 4 5 6 7
  p           q
n=2
1 2
len - n - 1
'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next: return None
        p = head
        q = None

        for i in range(n):
            p = p.next
        
        while p:
            p = p.next
            if not q: q = head
            else: q = q.next
        
        if not q: return head.next
        q.next = q.next.next
    
        return head