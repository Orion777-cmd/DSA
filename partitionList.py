# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
 
        leftCurr = leftHead = ListNode(0)
        rightCurr = rightHead = ListNode(0)
        current = head
        
        while current:
            if current.val < x:
                leftCurr.next = current
                leftCurr = leftCurr.next
                
            else:
                rightCurr.next = current
                rightCurr = rightCurr.next
                
            current = current.next
            
        rightCurr.next = None
        leftCurr.next = rightHead.next
		
        return leftHead.next
