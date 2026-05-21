class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1

        newList = None
        if list1.val > list2.val:
            newList = list2
            list2 = list2.next
        else:
            newList = list1
            list1 = list1.next
        
        p = newList
        while list1 and list2: 
            if list1.val > list2.val:
                p.next = list2
                list2 = list2.next
            else:
                p.next = list1
                list1 = list1.next
            p = p.next

        if not list2:
            p.next = list1
        else:
            p.next = list2
        
        return newList















