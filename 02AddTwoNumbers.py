# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry, total = 0,0 
        l3 = ListNode()
        res = l3
        while l1 or l2 or carry: 
            d1, d2 = 0,0
            if l1 : 
                d1 = l1.val     
                l1 = l1.next
            if l2 : 
                d2 = l2.val     
                l2 = l2.next
            total = d1+d2+carry
            carry = total // 10 
            l3.next = ListNode(total % 10)
            l3 = l3.next
        return res.next

      
