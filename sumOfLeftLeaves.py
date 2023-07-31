# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        sum_ = 0
        def dfs(root, sign=False):
            nonlocal sum_
            if not root: return 

            if not root.left and not root.right and sign:
                sum_ += root.val
            
            dfs(root.left, sign=True)
            dfs(root.right, sign=False)

            return 
        
        dfs(root)
        return sum_

