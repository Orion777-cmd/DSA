# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def dfs(node: Optional[TreeNode], res: list)-> list:
            if not node:
                return 
            if not node.right and not node.left:
                res.append(node.val)
            
            dfs(node.left, res)
            dfs(node.right, res)
            return res
        treeOne = dfs(root1, [])
        treeTwo = dfs(root2, [])
        if len(treeOne) != len(treeTwo):
            return False
        
        for i in range(len(treeOne)):
            if treeOne[i]  != treeTwo[i]:
                return False
        return True
