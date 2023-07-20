# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head: return 
        
        def recursion(head):
            
            if not head:
                return
            
            head.next = recursion(head.next)
            return head.next if(head.next and head.val < head.next.val) else head
             
        return recursion(head)
        

