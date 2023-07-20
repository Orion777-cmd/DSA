# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        dummy = head 
        fast = head
        if not head or not head.next: return None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        if slow == head: return head.next
        prev = dummy
        while prev.next != slow :
            prev = prev.next
        
        prev.next = slow.next
        return dummy
