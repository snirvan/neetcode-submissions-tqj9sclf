# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2:
            if l1:
                v1 = l1.val
            else:
                v1 = 0
            if l2:
                v2 = l2.val
            else:
                v2 = 0
            sum = v1 + v2 + carry
            curr.next = ListNode(sum%10)
            curr = curr.next
            carry = sum // 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry != 0:
            curr.next = ListNode(carry)

        return dummy.next


# 5, 3, 6
# 7, 3, 5

# 2 7 


# currplace = 12 % 10
# carry = 12 / 10

# find remainder of sum make ndoe with that value
# keep last made node
# when new node connect last node with this