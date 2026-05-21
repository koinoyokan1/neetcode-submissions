# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans = ListNode()
        heap = []

        i = 0
        for l in lists:
            if l:
                heapq.heappush(heap, (l.val, i, l))
                i += 1
        print('initial heap', list(heap))
        p = ans
        while heap:
            val, i, nxt = heapq.heappop(heap)
            ans.next = ListNode(val)
            ans = ans.next
            if nxt.next: heapq.heappush(heap, (nxt.next.val, i, nxt.next))
        
        return p.next
