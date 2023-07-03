# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head: return
        array = []
        while head:
            array.append(head.val)
            head = head.next
      
        array.pop(len(array)-n)
        current = ListNode()
        dummy = current
        for i in range(len(array)):
            data = ListNode(array[i])
            current.next = data
            current = data
        return dummy.next
