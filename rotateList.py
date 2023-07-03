# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:return
        array = []
        while head:
            array.append(head.val)
            head =  head.next

        while k >= len(array):
            k %= len(array)
        def rotateArray(num):
            for i in range(num):
                temp = array.pop()
                array.insert(0, temp)
        
        rotateArray(k)
        current = ListNode()
        dummy = current
        for i in range(len(array)):
            data = ListNode(array[i])
            current.next = data
            current = data
        return dummy.next
