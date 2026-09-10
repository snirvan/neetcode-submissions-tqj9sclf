# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head,head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        right = slow.next
        slow.next = None
        prev = None

        while right:
            temp = right.next
            right.next = prev
            prev = right
            right = temp
        
        
        right = prev
        left = head
        new = ListNode()
        start = new
        while right:
            templ = left.next
            tempr = right.next
            new.next = left
            left.next = right
            right.next = None
            new = right
            left = templ
            right = tempr
        new.next = left
        
            
