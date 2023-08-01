# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, max_ , min_):
            if not root:
                return True
            
            elif root.val >= max_ or root.val <= min_:
                return False
            
            else:
                return dfs(root.left , root.val, min_) and dfs(root.right, max_, root.val)
        
        return dfs(root, float('inf'), float('-inf'))
