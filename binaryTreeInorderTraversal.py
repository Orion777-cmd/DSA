# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root==None: return []
        val = []  
        def inorder( root):
            if root != None and (root.left != None):
                inorder(root.left)
            val.append(root.val)
            if root != None and root.right != None:
                inorder(root.right)
        inorder(root)
        return val
