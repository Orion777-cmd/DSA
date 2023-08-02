# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def binarySearch(left, right):
            if left >= right:
                return
            
            mid = (left + right)// 2

            node = TreeNode(nums[mid])
            node.left = binarySearch(left, mid)
            node.right = binarySearch(mid+1, right)

            return node
        
        return binarySearch(0, len(nums))

            
            
