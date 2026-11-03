# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        curr = head
        ans = 0
        stack = []
        while curr:
            stack.append(curr.val)
            curr = curr.next
        print(stack)
        i=0
        j=len(stack)-1
        while i<j:
            curr_sum = stack[i] + stack[j]
            if curr_sum > ans:
                ans = curr_sum
            i+=1
            j-=1
        return ans      