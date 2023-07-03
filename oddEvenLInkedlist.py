# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = ListNode()
        dummy = odd
        even = ListNode()
        dummy1 = even
        oddity = True
        while head:
            if oddity:
                odd.next = head
                odd = head
                oddity = False
            elif not oddity:
                even.next = head
                even = head
                oddity = True
            head = head.next
        odd.next = dummy1.next
        even.next = None
        return dummy.next
