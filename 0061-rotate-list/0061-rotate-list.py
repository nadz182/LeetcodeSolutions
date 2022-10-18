# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k <=0:
            return head
        
        listLen = 1
        lastNode = head
        
        while lastNode.next:
            lastNode = lastNode.next
            listLen += 1
        lastNode.next = head
        k %= listLen
        skip = listLen - k
        lastNodeRotated = head
        
        for i in range(skip-1):
            lastNodeRotated = lastNodeRotated.next
        head = lastNodeRotated.next
        lastNodeRotated.next = None
        return head