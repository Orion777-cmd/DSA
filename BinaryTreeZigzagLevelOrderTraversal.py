# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = collections.deque()
        queue.append(root)
        zigzag = False
        while queue:
            length = len(queue)
            level = []
            for i in range(length):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level and zigzag:
                level.reverse()
                res.append(level)
            if level and not zigzag:
                res.append(level)
            zigzag = not zigzag
        return res
