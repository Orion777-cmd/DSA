# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)

        stack = [root]
        while stack:
            parent = stack.pop()

            if parent and parent.left:
                graph[parent.val].append(parent.left.val)
                graph[parent.left.val].append(parent.val)
                stack.append(parent.left)
            if parent and parent.right:
                graph[parent.val].append(parent.right.val)
                graph[parent.right.val].append(parent.val)
                stack.append(parent.right)
            
        res = 0
        def dfs(start, minute, visited):
            nonlocal res
            if start in visited:
                res = max(res, minute)
                return 
            visited.add(start)
            for neighbor in graph[start]:
                dfs(neighbor, minute+1, visited)
            
            return
        dfs(start, -1, set())
        return res

