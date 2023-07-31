# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        queue = [(root, root.val)]
        while queue:
            parent, value = queue.pop()
            if not parent.right and not parent.left:
                if targetSum == value: return True
                else:
                    continue
            if parent.left:
                queue.append((parent.left, value + parent.left.val))
            
            if parent.right:
                queue.append((parent.right, value + parent.right.val))
        return False
        
