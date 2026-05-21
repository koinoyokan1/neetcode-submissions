# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans, p = None, None
        carry = 0

        while l1 and l2:
            num = l1.val + l2.val + carry
            carry = num // 10
            num = num % 10

            n = ListNode(num)
            if not ans: 
                ans = n 
                p = ans
            else: 
                p.next = n
                p = p.next

            l1 = l1.next
            l2 = l2.next

        if not l1 and not l2:
            if carry: p.next = ListNode(1)
            return ans
        
        if l2: l1, l2 = l2, l1
        
        n = l1
        while n:
            if n.val == 9 and carry: 
                p.next = ListNode(0)
                n = n.next
                p = p.next
                continue
            if carry:
                p.next = ListNode(n.val+1)
                return ans

            p.next = n
            return ans

        if carry:
            p.next = ListNode(1)
            return ans  
        return ans



