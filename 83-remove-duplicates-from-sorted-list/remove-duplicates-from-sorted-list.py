# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head
        ptr = head
        while ptr.next:
            if ptr.val == ptr.next.val:
                ptr.next = ptr.next.next
            else:
                ptr = ptr.next
        return head