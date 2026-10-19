# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if (not head) or (not head.next):
            return head
        stack = []
        curr = head
        stack.append(curr.val)
        while curr.next and curr.next.next:
            # stack.append(curr.val)
            curr = curr.next.next
            stack.append(curr.val)
        curr = head.next
        while curr and curr.next:
            stack.append(curr.val)
            curr = curr.next.next
        curr = head
        i=0
        while i<len(stack):
            curr.val = stack[i]
            curr = curr.next
            i+=1
        return head