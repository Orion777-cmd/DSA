# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(root, comp):
            if not root:
                return
            nonlocal res
            if root.val >= comp:
                res += 1
            dfs(root.left, max(comp, root.val))
            dfs(root.right, max(comp, root.val))
        dfs(root, root.val)
        return res
            
