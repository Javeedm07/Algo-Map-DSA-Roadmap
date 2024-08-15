class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        ptr1, ptr2 = head, head.next
        while ptr2:
            if ptr1.val != ptr2.val:
                ptr1 = ptr1.next
                ptr2 = ptr2.next
            else:
                ptr2 = ptr2.next
                ptr1.next = ptr2
        ptr1.next = None
        return head
