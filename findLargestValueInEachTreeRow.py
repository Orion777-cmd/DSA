# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return
        queue = [root]
        res =[]
        while queue:

            temp = []
            max_val = float('-inf')

            while queue:
                parent = queue.pop(0)
                max_val = max(max_val, parent.val if parent else float('-inf'))
                if parent and parent.left: temp.append(parent.left)
                if parent and parent.right: temp.append(parent.right)
            
            res.append(max_val)
            queue = temp
        
        return res

            
