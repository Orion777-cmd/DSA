# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        mode = defaultdict(int)
        stack = [root]

        while stack:
            temp = stack.pop()
            
            mode[temp.val] += 1

            if temp.left: stack.append(temp.left)
            if temp.right: stack.append(temp.right)
        mode = dict(sorted(mode.items(), key = lambda x:x[1], reverse=True))
        res = []
        max_ = 0
       
        for key, val in mode.items():
            if val >= max_:
                max_ = val
                res.append(key)
        return res
