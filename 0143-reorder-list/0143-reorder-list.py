# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        def reverse(head):
            prev = None
            while head:
                next = head.next
                head.next = prev 
                prev = head
                head = next
            return prev
        
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        firsthead = head
        secondhead = reverse(slow)
        
        while firsthead and secondhead:
            temp = firsthead.next
            firsthead.next = secondhead
            firsthead = temp 
            
            temp = secondhead.next
            secondhead.next = firsthead
            secondhead = temp
        
        if firsthead is not None:
            firsthead.next = None