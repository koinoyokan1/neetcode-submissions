# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans, p = None, None
        carry = 0

        while l1 or l2:
            l1val, l2val = 0, 0
            if l1: l1val = l1.val
            if l2: l2val = l2.val

            num = l1val + l2val + carry
            carry = num // 10
            num = num % 10

            n = ListNode(num)
            if not ans: 
                ans = n 
                p = ans
            else: 
                p.next = n
                p = p.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        if carry: p.next = ListNode(1)

        return ans



