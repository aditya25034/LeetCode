# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        a, b =[], []
        cur , curr = l1, l2
        while cur or curr:
            if cur:
                a.append(cur.val)
                cur = cur.next
            if curr:
                b.append(curr.val)
                curr = curr.next

        m = "".join(map(str,a))
        n = "".join(map(str,b))

        m, n = m[::-1], n[::-1]

        p = int(m) + int(n)

        dummy = ListNode(0)
        r=dummy

        if p==0:
            return r

        while p>0:
            rem=p%10
            a=ListNode(rem)
            r.next=a
            r=r.next
            p//=10
        
        return dummy.next