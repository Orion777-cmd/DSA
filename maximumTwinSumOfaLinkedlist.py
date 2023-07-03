# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        array= []
        while head:
            array.append(head.val)
            head = head.next
        res = 0
        i = 0
        j = len(array)-1
        while i < j:
            res = max(array[i] + array[j], res)
            i += 1
            j -= 1
        return res
