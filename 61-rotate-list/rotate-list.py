# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        count =0
        curr = head
        while curr:
            count +=1
            curr = curr.next
        if count:
            k = k%count
        if head == None or k==0 or count ==k:
            return head
        k = k%count
        
        slow = head
        fast = head
        for i in range(k):
            fast = fast.next
        
        while fast.next != None :
            slow = slow.next
            fast = fast.next
        
        temp = slow.next
        slow.next = None

        fast.next = head

        head = temp

        return head