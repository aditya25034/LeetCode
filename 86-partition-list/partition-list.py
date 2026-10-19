# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        if not head or not head.next:
            return head
        stack = []
        curr = head
        while curr:
            if curr.val < x:
                stack.append(curr.val)
                curr = curr.next
            else:
                curr = curr.next
        curr = head
        while curr:
            if curr.val >= x:
                stack.append(curr.val)
                curr = curr.next
            else:
                curr = curr.next
        i=0
        curr = head
        while i < len(stack):
            curr.val = stack[i]
            curr = curr.next
            i+=1
        return head