# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        current, prev = head, None
        i=0
        while current and i < left-1:
            prev = current
            current = current.next
            i+=1
            
        lastNodeFirstPart = prev
        lastNodeSubPart = current
        next = None
        i=0
        
        while current and i < right-left+1:
            next = current.next
            current.next = prev
            prev = current
            current = next
            i+=1
        
        if lastNodeFirstPart:
            lastNodeFirstPart.next = prev
        else:
            head = prev
        
        lastNodeSubPart.next = current
        return head