# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        list1 = []
        while head:
            list1.append(head.val)
            head = head.next
        while left <= right:
            list1[left-1], list1[right-1] = list1[right-1], list1[left-1]
            left += 1
            right -= 1
       
        head = ListNode()
        dummy = head
        for i in range(len(list1)):
            data = ListNode(list1[i])
            head.next = data
            head = data

        return dummy.next
