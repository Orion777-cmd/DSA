# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head : return 
        pointer1 , pointer2 = head,head
        while pointer2.next and pointer2.next.next:
            pointer1 = pointer1.next
            pointer2 = pointer2.next.next
            if pointer1 == pointer2 :
                break
        if not pointer2.next or not pointer2.next.next: return
        pointer = head
        while pointer:
            if pointer == pointer1:
                return pointer
            pointer =  pointer.next
            pointer1 = pointer1.next
        return
        
            
