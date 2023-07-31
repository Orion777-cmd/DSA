# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        queue = [root]
        depth = 0
        while queue:
            

            new = []
            while queue:
                temp = queue.pop(0)

                if temp and temp.left: new.append(temp.left)
                if temp and temp.right: new.append(temp.right)

            depth += 1
            queue = new
        
        return depth
