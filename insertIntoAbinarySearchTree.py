# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = TreeNode(val)
        if not root:
            root = node
            return root
        cur = root
        while cur:
            if val < cur.val:
                if cur.left == None:
                    cur.left = node
                    return root
                cur = cur.left
            else:
                if cur.right == None:
                    cur.right = node
                    return root
                cur = cur.right
