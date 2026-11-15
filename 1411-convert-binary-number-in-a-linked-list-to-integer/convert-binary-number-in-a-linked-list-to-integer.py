# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode | None) -> int:
        ans =0
        power =0
        number = []
        curr =head
        while curr:
            number.append(curr.val)
            curr = curr.next
        for i in range(len(number)):
            popped = number.pop()
            if popped:
                ans+= 2**power
                power+=1
            else:
                power+=1
        return ans