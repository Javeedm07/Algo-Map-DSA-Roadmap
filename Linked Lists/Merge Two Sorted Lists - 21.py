class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = list1
        ptr2 = list2
        dummy = curr = ListNode()
        while ptr1 and ptr2:
            if ptr1.val < ptr2.val:
                curr.next = ptr1
                ptr1 = ptr1.next
            else:
                curr.next = ptr2
                ptr2 = ptr2.next
            curr = curr.next
        if ptr1:
            curr.next = ptr1
        if ptr2:
            curr.next = ptr2
        return dummy.next
