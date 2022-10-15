# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
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
        
        secondHead = reverse(slow)
        copySecondHead = secondHead
        
        while head and secondHead:
            if head.val != secondHead.val:
                break
            head = head.next
            secondHead = secondHead.next
        
        reverse(copySecondHead)
        
        if not head or not secondHead:
            return True
        return False