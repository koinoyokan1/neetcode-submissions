# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        
        while p:
            q = p.next
            if not q: break 
            val = math.gcd(p.val, q.val)
            mid = ListNode(val, q)
            p.next = mid
            p = q

        return head