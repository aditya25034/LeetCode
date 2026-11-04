# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        stack = []
        slow = head
        fast = head
        ans = 0
        while fast.next.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        stack.append(slow.val)
        curr = slow.next
        print(curr.val)
        print(stack)
        while stack:
            curr_sum = curr.val + stack.pop()
            if curr_sum > ans:
                ans = curr_sum
            curr = curr.next
        return ans


