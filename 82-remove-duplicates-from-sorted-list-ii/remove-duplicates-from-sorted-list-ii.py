# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0 , head)
        if not head or not head.next:
            return head
        
        curr = head
        temp = dummy
        while curr and curr.next:
            if curr.val == curr.next.val:
                while curr.next and curr.val == curr.next.val: 
                    curr = curr.next
                temp.next =curr.next
                # if temp == head :
                #     temp = curr
                #     head = curr
                # else:
                #     temp.next = curr
             

            else:
                temp = temp.next
            curr = curr.next
                
        return dummy.next